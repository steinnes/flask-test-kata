bootstrap:
	rm -rf venv
	virtualenv -p python2.7 venv
	venv/bin/pip install -r requirements.txt
	venv/bin/python setup.py develop

integration_test:
	venv/bin/py.test tests/integration -v

unit_test:
	venv/bin/py.test tests/unit -v

test: unit_test integration_test

run:
	venv/bin/python calculator/app.py
