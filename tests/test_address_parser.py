from unittest.mock import patch, Mock

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


@patch("ez_address_parser.address_parser.load_data")
@patch("ez_address_parser.address_parser.sklearn_crfsuite")
def test_AddressParser_train(sklearn_crfsuite, load_data):
    with pytest.warns(UserWarning) as warnings:
        ap = AddressParser(use_pretrained=False)

    c1 = 0
    c2 = 0
    data = []
    X, y = [], []
    crf = Mock()

    load_data.return_value = (X, y)
    sklearn_crfsuite.CRF.return_value = crf

    ap.train(data, c1=c1, c2=c2)

    load_data.assert_called_once_with(data)

    sklearn_crfsuite.CRF.assert_called_once_with(
        algorithm="lbfgs",
        max_iterations=100,
        all_possible_transitions=True,
        c1=c1,
        c2=c2,
    )

    crf.fit.assert_called_once_with(X, y)
