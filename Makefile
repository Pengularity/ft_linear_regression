# PY		= python3
# VENV	= .venv


# all: train

# install:
# 	$(PY) -m venv $(VENV) && source $(VENV)/bin/activate && pip install -r requirements.txt

# train:
# 	$(PY) train.py --alpha 0.05 --epochs 20000

# predict:
# 	$(PY) predict.py

# plot:
# 	$(PY) -m bonus.plot

# precision:
# 	$(PY) -m bonus.precision

# bonus: precision plot

# clean:
# 	@echo "🧹 Cleaning temporary files..."
# 	@find . -name "*.py[co]" -delete
# 	@find . -type d -name "__pycache__" -exec rm -rf {} +
# 	@rm -f regression_plot.png model_params.txt
# 	@echo "✅ Clean complete."

# fclean: clean
# 	@echo "🧼 Full clean (removing model data)..."
# 	@rm -f thetas.json
# 	@echo "✅ Full clean complete."

# re: fclean all

# lint:
# 	@echo "🔍 Running pyflakes lint check..."
# 	@python3 -m pyflakes src || true


# .PHONY: all install train predict plot precision bonus clean fclean re lint


# ------------------------------
#  VARIABLES
# ------------------------------
IMAGE_NAME  = ft_linear_regression
CONTAINER_WORK_DIR = /usr/src/app
HOST_VOLUME = $(shell pwd)

ALPHA   ?= 0.05
EPOCHS  ?= 20000

# Base Docker parts (Split to allow inserting flags like -it)
DOCKER_PREFIX = docker run --rm -v "$(HOST_VOLUME):$(CONTAINER_WORK_DIR)"

# ------------------------------
#  MAIN TARGETS
# ------------------------------

all: train

build:
	docker build -t $(IMAGE_NAME) .

train: build
	$(DOCKER_PREFIX) $(IMAGE_NAME) python train.py --alpha $(ALPHA) --epochs $(EPOCHS)

predict: build
	$(DOCKER_PREFIX) -it $(IMAGE_NAME) python predict.py

# ------------------------------
#  BONUS & UTILS
# ------------------------------

plot: build
	$(DOCKER_PREFIX) $(IMAGE_NAME) python -m bonus.plot

precision: build
	$(DOCKER_PREFIX) $(IMAGE_NAME) python -m bonus.precision

bonus: precision plot

# ------------------------------
#  CLEANING
# ------------------------------

clean:
	@echo "🧹 Cleaning temporary files..."
	@rm -f regression_plot.png model_params.txt
	@rm -rf __pycache__ src/__pycache__ bonus/__pycache__
	@echo "✅ Clean complete."

fclean: clean
	@echo "🧼 Full clean (removing model data and Docker image)..."
	@rm -f thetas.json
	@# Move the heavy docker removal to fclean only
	@docker rmi -f $(IMAGE_NAME) 2>/dev/null || true
	@echo "✅ Full clean complete."

re: fclean all

# ------------------------------
#  DEV TOOLS
# ------------------------------

lint: build
	@echo "🔍 Running pyflakes lint check inside Docker..."
	$(DOCKER_PREFIX) $(IMAGE_NAME) python -m pyflakes src || true

.PHONY: all build train predict plot precision bonus clean fclean re lint