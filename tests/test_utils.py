import pytest

from ez_address_parser.utils import tokenize


@pytest.mark.parametrize(
    "address, tokens",
    [
        ("123 main st", ["123", "main", "st"]),
        ("123 main st, #456", ["123", "main", "st", "#", "456"]),
    ],
)
def test_tokenize(address, tokens):
    assert tokenize(address) == tokens
