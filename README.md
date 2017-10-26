Civ-Pytest
==========

This is an example project to demonstrate the usefulness of testing
and a number of ways we can test.
It uses the relatively famous Nuclear Ghandi bug from Civilisation as
motivation for the need to test as well as the bugs that are introduced here.

Installation
------------

To set up the environment and package to play with the simplest method is to clone this repository

    git clone https://github.com/malramsay64/civ-pytest.git

change directory into the repository

    cd civ-pytest

then assuming [conda](_conda) is installed run

    conda env create -f environment.yml

which will create a new python environment with all the required packages.
This can be activated with

    source activate civ-pytest  # `activate civ-pytest` for windows

finally to install the `civ-pytest` package run the command

    python setup.py develop

which will build the Cython files and install the package into the python runtime
while still being able to edit the files.

At this point tests can be run with

    pytest -v

[_conda]: https://conda.io/miniconda.html
