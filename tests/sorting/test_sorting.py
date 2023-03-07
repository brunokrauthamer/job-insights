from src.pre_built.sorting import sort_by
import pytest


@pytest.fixture
def generate_input_dict():
    return [
        {
            "min_salary": 3200,
            "max_salary": 15000,
            "date_posted": "2022-03-03"
        },
        {
            "min_salary": 1200,
            "max_salary": 5000,
            "date_posted": "2023-03-03"
        },
        {
            "min_salary": 12000,
            "max_salary": 100000,
            "date_posted": "2021-03-03"
        },
    ]


@pytest.fixture
def generate_output_dict():
    return [
        {
            "min_salary": 1200,
            "max_salary": 5000,
            "date_posted": "2023-03-03"
        },
        {
            "min_salary": 3200,
            "max_salary": 15000,
            "date_posted": "2022-03-03"
        },
        {
            "min_salary": 12000,
            "max_salary": 100000,
            "date_posted": "2021-03-03"
        },
    ]


def test_sort_by_criteria(generate_input_dict, generate_output_dict):
    sort_by(generate_input_dict, "min_salary")
    assert generate_input_dict == generate_output_dict
