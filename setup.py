"""
Setup file for backward compatibility.

Modern installations should use Poetry:
    poetry install

For legacy pip installations:
    pip install .
"""

from setuptools import setup

# Poetry handles all configuration via pyproject.toml
# This file exists only for backward compatibility with tools that require setup.py

setup()

