#!/usr/bin/python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'My project',
    'author' : 'Gu',
    'url' : 'URL to get it at.',
    'download_url' : 'Where to download it.',
    'author_email' : 'My email.',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages' : ['exp47'],
    'scripts' : [],
    'name' : 'projectname'
}

setup(**config)

    
