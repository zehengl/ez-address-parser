from string import digits
from .constants import direction_terms, street_types, unit_designators
from .utils import tokenize


def is_direction_term(token):
    return token.lower() in direction_terms


def is_street_type(token):
    return token.lower() in street_types


def is_unit_designator(token):
    return token.lower() in unit_designators


def relates_to_digit(token):
    if token.isdigit():
        return "all"
    elif set(token) & set(digits):
        return "some"
    else:
        return "none"


def relates_to_length(token):
    if token.isdigit():
        return f"d:{len(token)}"
    else:
        return f"w:{len(token)}"


def token_to_feature(token, name):
    return {
        f"{name}-is-directioin-term": is_direction_term(token),
        f"{name}-is-street-type": is_street_type(token),
        f"{name}-is-unit-designator": is_unit_designator(token),
        f"{name}-is-title": token.istitle(),
        f"{name}-is-alpha": token.isalpha(),
        f"{name}-token": False if token.isdigit() else token.lower(),
        f"{name}-relate-to-digit": relates_to_digit(token),
        f"{name}-relate-to-length": relates_to_length(token),
    }


def tokens_to_instance(tokens):
    instance = []
    for i, token in enumerate(tokens):
        feature = token_to_feature(token, "curr")
        if i > 0:
            token_prev = tokens[i - 1]
            feature.update(token_to_feature(token_prev, "prev"))
        else:
            feature.update({"begin-of-address": True})

        if i < len(tokens) - 1:
            token_next = tokens[i + 1]
            feature.update(token_to_feature(token_next, "next"))
        else:
            feature.update({"end-of-address": True})

        instance.append(feature)

    return instance


def transform(address):
    return tokens_to_instance(tokenize(address))


def load_data(data):
    X, y = [], []
    for address in data:
        tokens, labels = [], []
        for token, label in address:
            tokens.append(token)
            labels.append(label)
        X.append(tokens_to_instance(tokens))
        y.append(labels)

    return X, y
