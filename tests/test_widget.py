import pytest

from src.widget import mask_account_cart, get_data


@pytest.fixture
def type_cart_and_account_numbers():
    return ['Maestro 1596837868705199', 'Счет 64686473678894779589', 'MasterCard 7158300734726758',
            'Счет 35383033474447895560', 'Visa Classic 6831982476737658', 'Visa Platinum 8990922113665229',
            'Visa Gold 5999414228426353', 'Счет 73654108430135874305']


@pytest.mark.parametrize("type_cart_and_account_numbers, expected",
                         [('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                          ('Счет 64686473678894779589', 'Счет **9589'),
                          ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
                          ('Счет 35383033474447895560', 'Счет **5560'),
                          ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
                          ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
                          ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353'),
                          ('Счет 73654108430135874305', 'Счет **4305')])
def test_mask_account_cart_correct(type_cart_and_account_numbers, expected):
    assert mask_account_cart(type_cart_and_account_numbers) == expected


@pytest.fixture
def date():
    return ['2018-07-11T02:26:18.671407', '2008-12-10T02:33:26.985407', '2121-03-02T02:52:02.671564']


@pytest.mark.parametrize("date, expected", [('2018-07-11T02:26:18.671407', '11.07.2018'),
                                            ('2008-12-10T02:33:26.985407', '10.12.2008'),
                                            ('2121-03-02T02:52:02.671564', '02.03.2121')])
def test_get_data_correct(date, expected):
    assert get_data(date) == expected
