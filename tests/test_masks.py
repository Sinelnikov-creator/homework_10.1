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




