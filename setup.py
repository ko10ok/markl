import pathlib

from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent
README = open("README.md").read()
setup(
    name="markl",
    version="0.0.4",
    description=".tsx locator marker",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Yuriy Sagitov",
    author_email="pro100.ko10ok@gmail.com",
    python_requires=">=3.8.0",
    url="https://github.com/ko10ok/markl",
    license="Apache-2.0",
    packages=find_packages(exclude=("tests",)),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "markl-do = markl:mark",
            "markl-rollback = markl:rollback"
        ],
    },
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
