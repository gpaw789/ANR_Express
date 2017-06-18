# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ANR Express',
    version='0.2',
    description='Express form for Philips ANR',
    long_description=readme,
    author='G Paw',
    author_email='georgepaw789(at)hotmail.com',
    url='https://github.com/kennethreitz/samplemod',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

