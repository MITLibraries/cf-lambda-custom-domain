SHELL=/bin/bash
DATETIME:=$(shell date -u +%Y%m%dT%H%M%SZ)

help: # preview Makefile commands
	@awk 'BEGIN { FS = ":.*#"; print "Usage:  make <target>\n\nTargets:" } \
/^[-_[:alpha:]]+:.?*#/ { printf "  %-15s%s\n", $$1, $$2 }' $(MAKEFILE_LIST)

## ---- Dependency commands ---- ##

install: # install Python dependencies
	pipenv install --dev
	pipenv run pre-commit install

update: install # update Python dependencies
	pipenv clean
	pipenv update --dev

## ---- Unit test commands ---- ##

test: # run tests and print a coverage report
	pipenv run coverage run --source=lambdas -m pytest -vv
	pipenv run coverage report -m

coveralls: test # write coverage data to an LCOV report
	pipenv run coverage lcov -o ./coverage/lcov.info

## ---- Code quality and safety commands ---- ##

lint: black safety # run linters

black: # run 'black' linter and print a preview of suggested changes
	pipenv run black --check --diff .

safety: # check for security vulnerabilities and verify Pipfile.lock is up-to-date
	pipenv check
	pipenv verify

lint-apply: # apply changes with 'black' and resolve 'fixable errors' with 'ruff'
	black-apply 

black-apply: # apply changes with 'black'
	pipenv run black .

## Terraform Generated Makefile additions        ##
## ---- Local Developer Deployment Commands ---- ##
        
dev-deploy:
	rm -rf cf-lambda-custom-domain.py.zip
	zip -j cf-lambda-custom-domain.py.zip lambdas/*
	aws s3api put-object --bucket shared-files-222053980223 --body cf-lambda-custom-domain.py.zip --key files/cf-lambda-custom-domain.py.zip
	rm -rf cf-lambda-custom-domain.py.zip
