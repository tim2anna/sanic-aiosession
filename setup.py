#!/usr/bin/python3
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name='sanic-aiosession',
    version='0.1',
    description=(
        'sanic-aiosession is an extension for Sanic that adds support for Server-side Session to your application.'
    ),
    long_description=open('README.md').read(),
    author='Tim.Wang',
    author_email='191996155@qq.com',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/wanghao524151/sanic-aiosession',
    install_requires=[
        'sanic>=0.6.0',
        'aioredis>=0.3.3',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)