#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import sys

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'django-heroku-restrict-ip'
DESCRIPTION = 'Restrict access to Heroku-based Django apps by IP address.'
URL = 'https://github.com/celerityweb/django-heroku-restrict-ip'
EMAIL = 'website-admin@celerity.com'
AUTHOR = 'Celerity'

# What packages are required for this module to be executed?
REQUIRED = [
    'ipcalc', 'django-ipware'
]

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

# Where the magic happens:
setup(
    name=NAME,
    version='0.1.0',
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    include_package_data=True,
    license='BSD',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)