PYTHON = python3
PIP = pip3

prep:
	mkdir -p logs tmp data results

run: prep
	$(PYTHON) src/pipeline.py

debug:
	$(PYTHON) src/pipeline.py --debug

lint:
	pylint src/

install:
	 $(PIP) install -r requirements.txt

clean:
	find . -type f -name \*.pyc -exec rm {} \;
	rm -rf dist *.egg-info .coverage .DS_Store logs tmp

clean-data:
	rm -rf data

clean-results:
	rm -rf results

clean-full: clean clean-data clean-results
