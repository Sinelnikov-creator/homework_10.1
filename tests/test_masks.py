import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def card_number():
    return ['7000792289606361', '2202203248079137', '558620000054233776', '558620005423qwer']


@pytest.mark.parametrize("card_number, expected", [('7000792289606361', '7000 79** **** 6361'),
                                                   ('2202203248079137', '2202 20** **** 9137'),
                                                   ('558620000054233776', '5586 20** **** 3776'),
                                                   ('558620005423qwer', '5586 20** **** qwer')])
def test_get_mask_card_number_correct(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_invalid_len_card():
    with pytest.raises(ValueError):
        get_mask_card_number('1234')


@pytest.fixture
def account_number():
    return ['73654108430135874305', '7365410855600635876894', '7365410888773587qwer']


@pytest.mark.parametrize("account_number, expected", [('73654108430135874305', '**4305'),
                                                      ('7365410855600635876894', '**6894'),
                                                      ('7365410888773587qwer', '**qwer'),])
def test_get_mask_account_correct(account_number, expected):
    assert get_mask_account(account_number) == expected


def test_get_mask_account_invalid_len():
    with pytest.raises(ValueError):
        get_mask_account('1234')
