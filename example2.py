import pickle
from pathlib import Path

from ez_address_parser import AddressParser

ap = AddressParser(use_pretrained=False)

here = Path(__file__).parent.absolute()

with open(here / "ez_address_annotator/data/data.pkl", "rb") as f:
    data = pickle.load(f)

print(f"{len(data)} labelled addresses are used to create this pretrained model")

ap.train(data)

address = input("Address: ")
result = ap.parse(address)
for token, label in result:
    print(f"{token:20s} -> {label}")
