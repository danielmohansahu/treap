#!/usr/bin/env python

from distutils.core import setup

setup(name='pytreap',
      version='1.0',
      description='Python implementation of a Binary Tree / Heap data structure.',
      author='Daniel M. Sahu',
      author_email='danielmohansahu@gmail.com',
      url='https://github.com/danielmohansahu/treap',
      scripts=['scripts/run_tests', 'scripts/enpm809x'],
      data_files=[("scripts",["scripts/textbook.txt"])],
      requires=["typing", "unittest"],
      packages=['pytreap']
     )
