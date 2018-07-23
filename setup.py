from setuptools import setup
setup(
    name = 'PythonCLI',
    version = '0.1.0',
    packages = ['PythonCLI'],
    entry_points = {
        'console_scripts': [            
			'PythonCLI = PythonCLI.__main__:main'
        ]
    })