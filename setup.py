#!/usr/bin/env python

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "Click>=7.0",
    "iso8601",
    "htimeseries>=1.1,<2",
    "affine",
    "simpletail",
    "gdal>=1.10,<3",
]

test_requirements = []

setup(
    author="Antonis Christofides",
    author_email="antonis@antonischristofides.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    description="Utilities for spatial integration of time series",
    entry_points={"console_scripts": ["spatialize=hspatial.cli:main"]},
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords="hspatial",
    name="hspatial",
    packages=find_packages(include=["hspatial"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/openmeteo/hspatial",
    version="0.1.0.dev0",
    zip_safe=False,
)
