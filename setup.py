from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md")) as f:
    long_description = f.read()

with open(path.join(here, "requirements.txt")) as f:
    requirements = f.read().splitlines()

setup(
    name="ez-address-parser",
    packages=["ez_address_parser"],
    entry_points={"console_scripts": []},
    include_package_data=True,
    package_data={},
    install_requires=requirements,
    setup_requires=["setuptools_scm", "pytest-runner"],
    use_scm_version=True,
    tests_require=["pytest"],
    test_suite="tests",
    author="Zeheng li",
    author_email="imzehengl@gmail.com",
    maintainer="Zeheng li",
    maintainer_email="imzehengl@gmail.com",
    description="An address parser for Canadian postal addressess",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zehengl/ez-address-parser",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
