from src.pre_built.sorting import sort_by
import pytest


@pytest.fixture
def list():
    return [
        {'min_salary': 1000, 'max_salary': 2000, 'date_posted': '2020-05-04'},
        {'min_salary': 1500, 'max_salary': 2500, 'date_posted': '2020-06-03'},
        {'min_salary': 2000, 'max_salary': 3000, 'date_posted': '2020-07-02'},
        {'min_salary': 2500, 'max_salary': 4000, 'date_posted': '2020-08-01'},
    ]


def test_sort_by_criteria(list):
    sort_by(list, 'max_salary')
    assert list[0]['max_salary'] == 4000
    assert list[1]['max_salary'] == 3000
    assert list[2]['max_salary'] == 2500
    assert list[3]['max_salary'] == 2000

    sort_by(list, 'min_salary')
    assert list[0]['min_salary'] == 1000
    assert list[1]['min_salary'] == 1500
    assert list[2]['min_salary'] == 2000
    assert list[3]['min_salary'] == 2500

    sort_by(list, 'date_posted')
    assert list[0]['date_posted'] == '2020-08-01'
    assert list[1]['date_posted'] == '2020-07-02'
    assert list[2]['date_posted'] == '2020-06-03'
    assert list[3]['date_posted'] == '2020-05-04'
