init:
	pip install -r requirements.txt

all_tests:
	python -m pytest tests

unit_tests:
	python -m pytest tests/unit_tests

integration_tests:
	python -m pytest tests/integration_tests