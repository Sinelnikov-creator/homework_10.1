import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def list_of_dicts():
    return [{'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'EXECUTED', 'date': '2018-10-14T08:21:33.419441'}]


#@pytest.mark.parametrize("list_of_dicts, expected",
#                        [{'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
#                         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#                         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#                        {'id': 615064591, 'state': 'EXECUTED', 'date': '2018-10-14T08:21:33.419441'}],
#                        [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#                        {'id': 615064591, 'state': 'EXECUTED', 'date': '2018-10-14T08:21:33.419441'}])
def test_filter_by_state(list_of_dicts):
    assert filter_by_state(list_of_dicts) == [
                          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                          {'id': 615064591, 'state': 'EXECUTED', 'date': '2018-10-14T08:21:33.419441'}]


def test_sort_by_date(list_of_dicts):
    assert sort_by_date(list_of_dicts) == [
        {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]


