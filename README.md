# ez-address-parser

![coding_style](https://img.shields.io/badge/code%20style-black-000000.svg)
[![time tracker](https://wakatime.com/badge/github/zehengl/ez-address-parser.svg)](https://wakatime.com/badge/github/zehengl/ez-address-parser)

## Install

    pip install ez-address-parser

    To install development version, please `pip install git+https://github.com/zehengl/ez-address-parser.git`.

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
