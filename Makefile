.venv/bin/activate: ## Create python virtual environment and install requirements in that environment
	python3 -m venv .venv
	. .venv/bin/activate && \
	python3 -m pip install -r requirements-dev.txt

.PHONY: ansible-lint
ansible-lint: .venv/bin/activate  ## Run ansible-lint
	. .venv/bin/activate && tox -e ansible-lint

%:  ## Run tox with the specified environment
	. .venv/bin/activate && tox exec -e run -- ansible-playbook ansible_collections/solid/example/playbooks/$*.yml

.PHONY: clean
clean: ## Clean all generated file
	rm ./ansible_collections/solid/example/playbooks/*.txt
