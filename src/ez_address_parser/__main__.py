import argparse

from . import AddressParser

parser = argparse.ArgumentParser(
    description="An address parser for Canadian postal addresses"
)
parser.add_argument("--address", required=True, help="address")
args = parser.parse_args()
address = args.address

ap = AddressParser()

if ap.is_address(address):
    print(ap.parse(address))
else:
    print("It's not likely to be an address")
