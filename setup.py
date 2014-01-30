# -*- coding: utf-8 -*-
"""Installer for this package."""

from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.0'

long_description = ''


setup(
    name='animals',
    version=version,
    description="A simple app",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='Plone Python',
    author='Arkadiusz Adamski',
    author_email='arkadiusz.adamski@stxnext.pl',
    url='',
    license='BSD',
    namespace_packages=['tutorial'],
    package_dir={'': 'src'},
    packages=find_packages('src', exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
)
