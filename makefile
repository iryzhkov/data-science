PYTHON = python3
PIP = pip3

run: prep
	$(PYTHON) src/main.py

prep:
	mkdir -p logs tmp data output

lint:
	pylint src/

install:
	 $(PIP) install -r requirements.txt

clean:
	find . -type f -name \*.pyc -exec rm {} \;
	rm -rf dist *.egg-info .coverage .DS_Store logs tmp data output
