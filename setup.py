try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'use full contact api from command line.',
    'author': 'Austin Ogilvie',
    'keywords': 'full contact wrapper',
    'author_email': 'a@yhathq.com',
    'version': '0.1',
    'install_requires': ['nose', 'docopt', 'requests'],
    'packages': ['fullcontact'],
    'include_package_data': True,
    'scripts': ['bin/fullcontact'],
    'zip_safe': False,
    'name': 'fullcontact',
    'license': 'MIT'
}

setup(**config)
