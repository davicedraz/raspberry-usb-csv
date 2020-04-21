"""Setup Module"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'Automatic .csv backup to USB Disks'
DESCRIPTION = 'Script for detecting a new USB disk and automatically copy the sensors readings to a .csv file'
URL = 'https://github.com/davicedraz/raspberry-usb-csv.git'
EMAIL = 'davioler@gmail.com.br'
AUTHOR = 'Davi Cedraz'
REQUIRES_PYTHON = '>=3.8.1'
VERSION = '0.1.0'
REQUIRED = ['pyserial', 'python-dotenv']
EXTRAS = {}

HERE = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(HERE, 'README.md'), encoding='utf-8') as f:
        LONG_DESCRIPTION = '\n' + f.read()
except FileNotFoundError:
    LONG_DESCRIPTION = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(
        exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    url=URL,
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT'
)
