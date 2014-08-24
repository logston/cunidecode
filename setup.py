#!/usr/bin/python

from setuptools import setup, Extension


setup(
    name='unidecode',
    version='0.0.1',
    description='ASCII transliterations of Unicode text',
    license='GPL',
    long_description=open("README").read(),
    author='Paul Logston',
    author_email='code@logston.me',

    ext_modules=[Extension('unidecode', ['unidecode.c'])],

    provides = [ 'unidecode' ],
    test_suite='tests.test_basic_2',
    classifiers = [
    "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
	"Programming Language :: Python",
	"Programming Language :: Python :: 2",
	"Topic :: Text Processing",
	"Topic :: Text Processing :: Filters",
	],
)
