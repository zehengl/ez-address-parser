import pytest

from ez_address_parser import AddressParser


def test_AddressParser_without_pretrained_model():
    with pytest.warns(UserWarning) as warnings:
        ap = AddressParser(use_pretrained=False)
        assert len(warnings) == 1
        assert (
            warnings[0].message.args[0]
            == "Run train() to learn from some existing labelled data"
        )
    with pytest.raises(RuntimeError) as errors:
        ap.parse("")
        assert "Model is not loaded" in str(errors.value)


def test_AddressParser_with_pretrained_model():
    ap = AddressParser()
    assert ap.parse("123 Main Streat S.W.") == [
        ("123", "StreetNumber"),
        ("Main", "StreetName"),
        ("Streat", "StreetType"),
        ("S", "StreetDirection"),
        ("W", "StreetDirection"),
    ]
