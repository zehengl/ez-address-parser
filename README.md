# ez-address-parser

[![Build Status](https://travis-ci.org/zehengl/ez-address-parser.svg?branch=master)](https://travis-ci.org/zehengl/ez-address-parser)
![coding_style](https://img.shields.io/badge/code%20style-black-000000.svg)
![PyPI - License](https://img.shields.io/pypi/l/ez-address-parser)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ez-address-parser)
![PyPI](https://img.shields.io/pypi/v/ez-address-parser)
[![time tracker](https://wakatime.com/badge/github/zehengl/ez-address-parser.svg)](https://wakatime.com/badge/github/zehengl/ez-address-parser)

An address parser for Canadian postal addressess

## Install

From [PyPi](https://pypi.org/project/ez-address-parser/)

    pip install ez-address-parser

From [GitHub](https://github.com/zehengl/ez-address-parser)

    pip install git+https://github.com/zehengl/ez-address-parser.git

## Test

    python setup.py test

## Develop

    pip install -r requirements-dev.txt

### Annotation

    python .\ez_address_annotator\data\convert.py
    python .\ez_address_annotator\data\create_seed.py
    label-studio start ez_address_annotator

### Pretrained Model

    python .\ez_address_annotator\data\export.py
    python .\create_pretrained_model.py
