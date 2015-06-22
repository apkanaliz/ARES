#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'droidsec',
    version = '1.alpha',
    packages = find_packages(),
    scripts = ['droidsec.py'],
    install_requires=['distribute'],
)