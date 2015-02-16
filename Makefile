test:
	PYTHONPATH=.:tests/ python -m unittest discover -v -s tests/ -p '*_test.py'
