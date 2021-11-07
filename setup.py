# -*- coding: utf-8 -*-
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version():
    """Get version from the package without actually importing it."""
    init = read('jarpc_clients/__init__.py')
    for line in init.split('\n'):
        if line.startswith('__version__'):
            return eval(line.split('=')[1])


setup(
    name='jarpc_clients',
    version=get_version(),
    packages=['jarpc_clients'],
    description='JARPC Clients',
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
)
