
PYTHON = python3
PIP = pip3

run:
	$(PYTHON) pipeline.py

install:
	 $(PIP) install -r requirements.txt -t ./

lint:
	pylint academic_paper_reviewer/ tests/

clean:
	find . -type f -name \*.pyc -exec rm {} \;
	rm -rf dist *.egg-info .coverage .DS_Store logs/*
