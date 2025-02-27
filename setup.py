#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from setuptools import setup, find_packages


PACKAGE = "ormantic"
URL = "https://github.com/awesometoolbox/ormantic"


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    with open(f"src/{package}/__init__.py") as f:
        return re.search(
            "__version__ = ['\"]([^'\"]+)['\"]", f.read()
        ).group(1)


def get_long_description():
    """
    Return the README.
    """
    with open("README.md", encoding="utf8") as f:
        return f.read()


setup(
    name=PACKAGE,
    version=get_version(PACKAGE),
    url=URL,
    license="BSD",
    description="Async ORM + Pydantic = Ormantic ❤️",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Awesome Toolbox",
    author_email="info@awesometoolbox.com",
    packages=find_packages("src/"),
    package_data={PACKAGE: ["py.typed"]},
    package_dir={'': 'src'},
    data_files=[("", ["LICENSE.md"])],
    install_requires=["databases>=0.2.1", "pydantic"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
