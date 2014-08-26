#!/usr/bin/python

from setuptools import setup, Extension


setup(
    name='cunidecode',
    version='0.0.2',
    description='ASCII transliterations of Unicode text',
    license='GPL',
    long_description=open("README.rst").read(),
    author='Paul Logston',
    author_email='code@logston.me',
    url = 'https://github.com/logston/cunidecode',
    download_url = 'https://github.com/logston/cunidecode/tarball/0.0.2',
    ext_modules=[Extension('cunidecode', ['cunidecode.c'])],
    provides = [ 'cunidecode' ],
    test_suite='tests',
    keywords = ['unicode', 'c', 'unidecode'],
    classifiers = [
    "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
	"Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
	"Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython",
	"Topic :: Text Processing",
	"Topic :: Text Processing :: Filters",
	],
)
