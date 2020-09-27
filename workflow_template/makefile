
PYTHON = python3
PIP = pip3

run:
	$(PYTHON) src/pipeline.py

debug:
	$(PYTHON) src/pipeline.py --debug

lint:
	pylint src/

install:
	 $(PIP) install -r requirements.txt -t ./

clean:
	find . -type f -name \*.pyc -exec rm {} \;
	rm -rf dist *.egg-info .coverage .DS_Store logs/*
