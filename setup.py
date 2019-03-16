# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='shoperapi',
      version='1.0.0',
      description='Magical Shoper REST API Client',
      url='http://github.com/chawel/python-shoper',
      author='Pawel Chaniewski',
      author_email='pawel@cwsi.com',
      license='MIT',
      packages=['shoperapi'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
