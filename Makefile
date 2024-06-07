.venv/bin/activate: ## Create python virtual environment and install requirements in that environment
	python3 -m venv .venv
	. .venv/bin/activate && \
	python3 -m pip install -r requirements-dev.txt

.PHONY: ansible-lint
ansible-lint: .venv/bin/activate  ## Run ansible-lint
	. .venv/bin/activate && tox -e ansible-lint

.PHONY: tests
tests:
	. .venv/bin/activate && tox -e tests
