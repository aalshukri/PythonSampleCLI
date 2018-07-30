# PythonSampleCLI

Repo to be used as a base skeleton for development of command line interface applications.

Adapted from https://github.com/kennethreitz/samplemod


## Todo

* implement inheritance class and testing

* implement virtual environment


## Running Instructions

> python sample --help

To output debugging to screen

> python sample -d

To output debugging to file

> python sample -d log.txt


### Using virtual env




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
 <virtual environment>
  pip install -r requirements.txt
  python start_server.py



## Resources


