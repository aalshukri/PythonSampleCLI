# PythonSampleCLI

This repository contains a basic skeleton for development of command line interface applications.

Adapted from https://github.com/kennethreitz/samplemod


## Running Instructions

> python sample --help

To output debugging to screen

> python sample -d

To output debugging to file

> python sample -d log.txt


### Using virtual environment

Install virtualenv

> pip install virtualenv

Test virtualenv

> virtualenv --version


To use virtualenv in production

> virtualenv my_project

> source my_project/bin/activate

Install requirements

> pip install -r requirements.txt

Run python app

> python sample -d

exit virtualenv

> deactivate


## Testing


> python tests/test_basic.py
> python tests/test_advanced.py

> python tests/test_funcs.py
> python tests/test_helpers.py
> python tests/test_MyClass.py

Run all tests

> python -m unittest discover tests/



## Deployment

How to deploy this python application on production server

see:
https://www.nylas.com/blog/packaging-deploying-python/

git-pull-pip-install-deploy.sh

git clone https://github.com/company/somerepo.git
cd /opt/myproject
pip install -r requirements.txt
python sample -d


