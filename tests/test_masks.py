import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def card_number():
    return ['7000792289606361', '2202203248079137', '5586200054233776']


@pytest.mark.parametrize("card_number, expected", [('7000792289606361', '7000 79** **** 6361'),
                                                   ('2202203248079137', '2202 20** **** 9137'),
                                                   ('5586200054233776', '5586 20** **** 3776'),])
def test_get_mask_card_number_correct(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_invalid_len_card():
    with pytest.raises(ValueError):
        get_mask_card_number('1234')


def test_get_mask_card_number_invalid_len_card_zero():
    with pytest.raises(ValueError):
        get_mask_card_number(' ')


@pytest.fixture
def account_number():
    return ['73654108430135874305', '73654108556635876894', '73654108887735873625']


@pytest.mark.parametrize("account_number, expected", [('73654108430135874305', '**4305'),
                                                      ('73654108556635876894', '**6894'),
                                                      ('73654108887735873625', '**3625'),])
def test_get_mask_account_correct(account_number, expected):
    assert get_mask_account(account_number) == expected


def test_get_mask_account_invalid_len():
    with pytest.raises(ValueError):
        get_mask_account('1234')


def test_get_mask_account_invalid_len_zero():
    with pytest.raises(ValueError):
        get_mask_account(' ')


