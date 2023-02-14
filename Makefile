init:
	pip install -r requirements.txt
init-dev:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
run:
	python -m program
test:
	python -m unittest discover -v -s tests/ -p '*_test.py'
