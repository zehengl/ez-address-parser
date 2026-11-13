<figure markdown>
![Logo](https://raw.githubusercontent.com/zehengl/ez-address-parser/refs/heads/main/logo.png){ width="100" }
</figure>

# ez-address-parser

A parser for Canadian postal addresses

## Usage

### Command Line Example

```bash
python -m ez_address_parser --address "123 Main St"
```

### Code Example

1. Use the pretrained model

    ```python
    from ez_address_parser import AddressParser

    ap = AddressParser()

    address = input("Address: ")
    if ap.is_address(address):
        result = ap.parse(address)
        for token, label in result:
            print(f"{token:20s} -> {label}")
    else:
        print("It's not likely to be an address")
    ```

2. Train a model

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
