#!/usr/bin/env python
from setuptools import setup

setup(
    name='hapipy',
    version='2.8.3',
    description="A python wrapper around HubSpot's APIs",
    long_description = open('README.md').read(),
    author='HubSpot Dev Team',
    author_email='devteam+hapi@hubspot.com',
    url='https://github.com/HubSpot/hapipy',
    download_url='https://github.com/HubSpot/hapipy/tarball/v2.8.2',
    license='LICENSE.txt',
    packages=['hapi', 'hapi.mixins'],
    install_requires=[
        'nose==1.1.2',
        'unittest2==0.5.1',
        'simplejson==2.2.1'
    ],
)
