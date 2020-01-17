import pytest

from ez_address_parser.constants import direction_terms, street_types, unit_designators
from ez_address_parser.features import (
    is_direction_term,
    is_street_type,
    is_unit_designator,
    relates_to_digit,
    relates_to_length,
    token_to_feature,
    tokens_to_instance,
)


@pytest.mark.parametrize(
    "token, result",
    list(zip(direction_terms, [True] * len(direction_terms))) + [("x", False)],
)
def test_is_direction_term(token, result):
    assert is_direction_term(token) == result


@pytest.mark.parametrize(
    "token, result",
    list(zip(street_types, [True] * len(street_types))) + [("x", False)],
)
def test_is_street_type(token, result):
    assert is_street_type(token) == result


@pytest.mark.parametrize(
    "token, result",
    list(zip(unit_designators, [True] * len(unit_designators))) + [("x", False)],
)
def test_is_unit_designator(token, result):
    assert is_unit_designator(token) == result


@pytest.mark.parametrize(
    "token, result", [("123", "all"), ("abc", "none"), ("123abc", "some")]
)
def test_relates_to_digit(token, result):
    assert relates_to_digit(token) == result


@pytest.mark.parametrize(
    "token, result", [("123", "d:3"), ("abc", "w:3"), ("123abc", "w:6")]
)
def test_relates_to_length(token, result):
    assert relates_to_length(token) == result


@pytest.mark.parametrize(
    "token, name, feature",
    [
        (
            "123",
            "curr",
            {
                "curr-is-directioin-term": False,
                "curr-is-street-type": False,
                "curr-is-unit-designator": False,
                "curr-is-title": False,
                "curr-is-alpha": False,
                "curr-token": False,
                "curr-relate-to-digit": "all",
                "curr-relate-to-length": "d:3",
            },
        ),
        (
            "Unit",
            "next",
            {
                "next-is-directioin-term": False,
                "next-is-street-type": False,
                "next-is-unit-designator": True,
                "next-is-title": True,
                "next-is-alpha": True,
                "next-token": "unit",
                "next-relate-to-digit": "none",
                "next-relate-to-length": "w:4",
            },
        ),
    ],
)
def test_token_to_feature(token, name, feature):
    assert token_to_feature(token, name) == feature


@pytest.mark.parametrize(
    "tokens, instance",
    [
        (
            ["123", "main", "street"],
            [
                {
                    "curr-is-directioin-term": False,
                    "curr-is-street-type": False,
                    "curr-is-unit-designator": False,
                    "curr-is-title": False,
                    "curr-is-alpha": False,
                    "curr-token": False,
                    "curr-relate-to-digit": "all",
                    "curr-relate-to-length": "d:3",
                    "begin-of-address": True,
                    "next-is-directioin-term": False,
                    "next-is-street-type": False,
                    "next-is-unit-designator": False,
                    "next-is-title": False,
                    "next-is-alpha": True,
                    "next-token": "main",
                    "next-relate-to-digit": "none",
                    "next-relate-to-length": "w:4",
                },
                {
                    "curr-is-directioin-term": False,
                    "curr-is-street-type": False,
                    "curr-is-unit-designator": False,
                    "curr-is-title": False,
                    "curr-is-alpha": True,
                    "curr-token": "main",
                    "curr-relate-to-digit": "none",
                    "curr-relate-to-length": "w:4",
                    "prev-is-directioin-term": False,
                    "prev-is-street-type": False,
                    "prev-is-unit-designator": False,
                    "prev-is-title": False,
                    "prev-is-alpha": False,
                    "prev-token": False,
                    "prev-relate-to-digit": "all",
                    "prev-relate-to-length": "d:3",
                    "next-is-directioin-term": False,
                    "next-is-street-type": True,
                    "next-is-unit-designator": False,
                    "next-is-title": False,
                    "next-is-alpha": True,
                    "next-token": "street",
                    "next-relate-to-digit": "none",
                    "next-relate-to-length": "w:6",
                },
                {
                    "curr-is-directioin-term": False,
                    "curr-is-street-type": True,
                    "curr-is-unit-designator": False,
                    "curr-is-title": False,
                    "curr-is-alpha": True,
                    "curr-token": "street",
                    "curr-relate-to-digit": "none",
                    "curr-relate-to-length": "w:6",
                    "prev-is-directioin-term": False,
                    "prev-is-street-type": False,
                    "prev-is-unit-designator": False,
                    "prev-is-title": False,
                    "prev-is-alpha": True,
                    "prev-token": "main",
                    "prev-relate-to-digit": "none",
                    "prev-relate-to-length": "w:4",
                    "end-of-address": True,
                },
            ],
        )
    ],
)
def test_tokens_to_instance(tokens, instance):
    assert tokens_to_instance(tokens) == instance
