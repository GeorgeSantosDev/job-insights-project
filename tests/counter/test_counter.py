import pytest
from src.pre_built.counter import count_ocurrences
from unittest.mock import mock_open, patch


@pytest.fixture
def csv_content():
    return '''
    job_title,company,state,city, industry,rating, id
    developer, AB, MG, BH, Finance, 4.0, 0
    developer, Ab, MG, BH, finance, 5.0, 1
    developer, ABD, MG, BH, Finance, 3.0, 2
    '''


def test_counter(csv_content):
    with patch("builtins.open", mock_open(read_data=csv_content)):
        assert count_ocurrences('data/jobs.csv', 'developer') == 3
        assert count_ocurrences('data/jobs.csv', 'Finance') == 3
