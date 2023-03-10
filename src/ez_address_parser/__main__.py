import argparse

from . import AddressParser

parser = argparse.ArgumentParser(
    description="An address parser for Canadian postal addresses"
)
parser.add_argument("--address", required=True, help="address")
args = parser.parse_args()
address = args.address

ap = AddressParser()

print(ap.parse(address))
