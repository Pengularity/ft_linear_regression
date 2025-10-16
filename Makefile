PY		= python3
VENV	= .venv


all: train

install:
	$(PY) -m venv $(VENV) && source $(VENV)/bin/activate && pip install -r requirements.txt

train:
	$(PY) train.py --alpha 0.05 --epochs 20000

predict:
	$(PY) predict.py

plot:
	$(PY) -m bonus.plot

precision:
	$(PY) -m bonus.precision

bonus: precision plot

clean:
	@echo "🧹 Cleaning temporary files..."
	@find . -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@rm -f regression_plot.png model_params.txt
	@echo "✅ Clean complete."

fclean: clean
	@echo "🧼 Full clean (removing model data)..."
	@rm -f thetas.json
	@echo "✅ Full clean complete."

re: fclean all

lint:
	@echo "🔍 Running pyflakes lint check..."
	@python3 -m pyflakes src || true


.PHONY: all install train predict plot precision bonus clean fclean re lint