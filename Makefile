PY=python

install:
	$(PY) -m pip install -r requirements.txt

train:
	$(PY) train.py --alpha 0.1 --epochs 1000

predict:
	$(PY) predict.py

plot:
	$(PY) plot.py

lint:
	python -m pyflakes src || true

clean:
	rm -f thetas.json *.png
