<div align="center">
    <img src="https://cdn2.iconfinder.com/data/icons/seo-and-website/100/SEO_search_word-512.png" alt="logo" height="196">
</div>

# ez-address-parser

[![pytest](https://github.com/zehengl/ez-address-parser/actions/workflows/pytest.yml/badge.svg)](https://github.com/zehengl/ez-address-parser/actions/workflows/pytest.yml)
![coding_style](https://img.shields.io/badge/code%20style-black-000000.svg)
![PyPI - License](https://img.shields.io/pypi/l/ez-address-parser)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ez-address-parser)
![PyPI](https://img.shields.io/pypi/v/ez-address-parser)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/ez-address-parser)
[![Downloads](https://pepy.tech/badge/ez-address-parser)](https://pepy.tech/project/ez-address-parser)

A parser for Canadian postal addresses

## Install

From [PyPi](https://pypi.org/project/ez-address-parser/)

    pip install ez-address-parser

From [GitHub](https://github.com/zehengl/ez-address-parser)

    pip install git+https://github.com/zehengl/ez-address-parser.git

## Usage

### Command Line

    python -m ez_address_parser --address <some-address>

### Code (with pretrained model)

```python
from ez_address_parser import AddressParser

ap = AddressParser()

address = input("Address: ")
result = ap.parse(address)
for token, label in result:
    print(f"{token:20s} -> {label}")
```

### Code (without pretrained model)

```python
from ez_address_parser import AddressParser

ap = AddressParser(use_pretrained=False)

data = [
    [
        ('123', 'StreetNumber'),
        ('Main', 'StreetName'),
        ('St', 'StreetType'),
        ('E', 'StreetDirection')
    ],
    ...
] # list of list of (<token>, <label>) tuple

ap.train(data)

address = input("Address: ")
result = ap.parse(address)
for token, label in result:
    print(f"{token:20s} -> {label}")
```

## Test

    python setup.py test

## Develop

    pip install -r requirements-dev.txt

### Annotation

    python ez_address_annotator/data/convert.py
    python ez_address_annotator/data/create_seed.py
    label-studio start ez_address_annotator

`label-studio` provides an ease of use interface for name entity recognition. See the below example.

![labeling-example](https://github.com/zehengl/ez-address-parser/raw/main/labeling-example.gif)

### Pretrained Model

    python ez_address_annotator/data/export.py
    python create_pretrained_model.py

130 annotated addresses are used to train a default model that comes with this package.

## Credits

- [Icon][1] by [Rakhmat Setiawan][2]

[1]: https://www.iconfinder.com/icons/3059893/find_magnifier_search_seo_word_icon
[2]: https://www.iconfinder.com/rsetiawan93
