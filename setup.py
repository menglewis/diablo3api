#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'requests'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='diablo3api',
    version='0.1.0',
    description='A Python API Wrapper for the Diablo 3 API',
    long_description=readme + '\n\n' + history,
    author='David Lewis',
    author_email='meng.lewis@gmail.com',
    url='https://github.com/menglewis/diablo3api',
    packages=[
        'diablo3api',
        'tests',
    ],
    package_dir={'diablo3api':
                 'diablo3api'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='diablo3api',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)