from string import digits
from .constants import direction_terms, street_types, unit_designators


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


def token_to_feature(token, name):
    return {
        f"{name}-is-directioin-term": is_direction_term(token),
        f"{name}-is-street-type": is_street_type(token),
        f"{name}-is-unit-designator": is_unit_designator(token),
        f"{name}-is-title": token.istitle(),
        f"{name}-relate-to-digit": relates_to_digit(token),
    }
