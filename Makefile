.venv/bin/activate: ## Create python virtual environment and install requirements in that environment
	python3 -m venv .venv
	. .venv/bin/activate && \
	python3 -m pip install -r requirements-dev.txt

.PHONY: ansible-lint
ansible-lint: .venv/bin/activate  ## Run ansible-lint
	. .venv/bin/activate && tox -e ansible-lint

%: .venv/bin/activate  ## Run tox with the specified environment
	. .venv/bin/activate && tox exec -e run -- ansible-playbook -i ansible_collections/solid/example/inventory.ini ansible_collections/solid/example/playbooks/$@.yml

.PHONY: clean
clean: ## Clean all generated files
	rm ./ansible_collections/solid/example/playbooks/*.txt

.PHONY: playbooks
playbooks: ## Show all available playbooks
	@ls -1 ansible_collections/solid/example/playbooks | sed '/\.yml/!d' | sed 's/.yml//g'

.PHONY: help
help: ## Show this help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
