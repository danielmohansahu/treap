#!/usr/bin/env python

from distutils.core import setup

setup(name='pytreap',
      version='1.0',
      description='Python implementation of a Binary Tree / Heap data structure.',
      author='Daniel M. Sahu',
      author_email='danielmohansahu@gmail.com',
      url='https://github.com/danielmohansahu/treap',
      scripts=['scripts/pytreap_run_tests', 'scripts/pytreap_enpm809x_results'],
      data_files=[("scripts",["scripts/textbook.txt"])],
      requires=["typing", "unittest"],
      packages=['pytreap', 'pytreap.tests']
     )
