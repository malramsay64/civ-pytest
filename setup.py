#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Malcolm Ramsay <malramsay64@gmail.com>
#
# Distributed under terms of the MIT license.

"""Command line tool to run simulations."""

from setuptools import find_packages, setup
from setuptools.extension import Extension

from Cython.Build import cythonize

extensions = [
    Extension(
        'civ._civ',
        ['civ/_civ.pyx'],
        libraries=['m'],
        include_dirs=[],
    ),
]

setup(
    name='civ',
    packages=find_packages(),
    ext_modules=cythonize(extensions),
    include_package_data=True,
)
