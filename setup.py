#!/usr/bin/python
# -*- coding:Utf-8 -*-

from setuptools import setup

setup(name='PyGenie',
      scripts=['pygenie'],
      version='svn-r25',
      description='cli tools to mesure python complexity',
      author='David Stenek',
      url='http://www.traceback.org/2008/03/31/measuring-cyclomatic-complexity-of-python-code/',
      packages=["genie"],
     )

# vim:set shiftwidth=4 tabstop=4 expandtab:
