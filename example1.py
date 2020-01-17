from ez_address_parser import AddressParser

ap = AddressParser()

address = input("Address: ")
result = ap.parse(address)
for token, label in result:
    print(f"{token:20s} -> {label}")
