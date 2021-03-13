#!/usr/bin/env python

from distutils.core import setup

setup(name='pytreap',
      version='1.0',
      description='Python implementation of a Binary Tree / Heap data structure.',
      author='Daniel M. Sahu',
      author_email='danielmohansahu@gmail.com',
      url='https://github.com/danielmohansahu/treap',
      scripts=['scripts/pytreap_run_tests.py', 'scripts/pytreap_enpm809x_results.py'],
      package_data={"pytreap.data": ["textbook.txt"]},
      requires=["typing", "unittest"],
      packages=['pytreap', 'pytreap.tests', 'pytreap.data']
     )
