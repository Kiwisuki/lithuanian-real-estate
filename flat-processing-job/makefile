env:
	pip install poetry
	poetry install
	poetry self add poetry-plugin-shell
	pip install pre-commit
	pre-commit install

requirements:
	poetry export --without-hashes --without development,notebooks -f requirements.txt -o requirements.txt

