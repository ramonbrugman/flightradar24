# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    package_license = f.read()

setup(
    name='flightradar24',
    version='0.3',
    description='Data library for Flight Radar 24',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Mehmet Korkmaz',
    author_email='mehmet@mkorkmaz.com',
    url='https://github.com/mkorkmaz/flightradar24',
    license=package_license,
    packages=find_packages(exclude=('tests', 'docs'))
)

