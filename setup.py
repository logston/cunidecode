#!/usr/bin/python

from distutils.core import Command
from setuptools import setup, Extension
from sys import version_info
import unittest

UNITTESTS = [
		"basic",
	]

class TestCommand(Command):
	user_options = [ ]

	def initialize_options(self):
		pass

	def finalize_options(self):
		pass

	def run(self):
		suite = unittest.TestSuite()

		if version_info[0] >= 3:
			version = "_3"
		else:
			version = "_2"

		suite.addTests(
			unittest.defaultTestLoader.loadTestsFromNames(
				"tests." + test + version for test in UNITTESTS) )

		result = unittest.TextTestRunner(verbosity=2).run(suite)

setup(name='cUnidecode',
      version='0.0.1',
      description='ASCII transliterations of Unicode text',
      license='GPL',
      long_description=open("README").read(),
      author='Paul Logston',
      author_email='code@logston.me',

      ext_modules=[Extension('cUnidecode', ['cunidecode.c'])],

      packages = [ 'unidecode' ],

      provides = [ 'unidecode' ],

      cmdclass = { 'test': TestCommand },

      classifiers = [
	"License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
	"Programming Language :: Python",
	"Programming Language :: Python :: 2",
	"Programming Language :: Python :: 3",
	"Topic :: Text Processing",
	"Topic :: Text Processing :: Filters",
	],
)
