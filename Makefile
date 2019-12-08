setup:
	virtualenv ./.venv/
	./.venv/bin/pip install flake8

lint:
	./.venv/bin/flake8 ./chap2
