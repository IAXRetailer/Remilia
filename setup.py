#!/usr/bin/env python
# coding=utf-8

from time import localtime, strftime
from setuptools import setup, find_packages
setup(
    name='remilia',
    version=strftime("%Y_%m_%d_%H_%M_%S", localtime()),
    description=(
        'Use python with dignity,here offer some utils'
    ),
    long_description=open('README.rst').read(),
    author='h2sxxa',
    author_email='H2Sxxa0w0@gmail.com',
    maintainer='h2sxxa',
    maintainer_email='H2Sxxa0w0@gmail.com',
    license='MIT License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/IAXRetailer/Remilia',
    classifiers=[
    'License :: OSI Approved :: MIT License',

    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    ],
)