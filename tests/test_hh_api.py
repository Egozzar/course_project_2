from src.hh_api import HHApi
from unittest.mock import patch


def test_hh_api_init(arguments_for_init):
    res = HHApi(*arguments_for_init)

    assert len(res.__dict__) == 4


def test_hh_api_init_wrong(arguments_for_init_wrong):
    res = HHApi(*arguments_for_init_wrong)

    assert len(res.__dict__) == 3


@patch("requests.get")
def test_get_vacancies(mock_get, arguments_for_init, part_answer__connect_to_api, part_answer_get_vacancies):
    res = HHApi(*arguments_for_init)
    mock_get.return_value.json.return_value = part_answer__connect_to_api
    mock_get.return_value.status_code = 200
    res.get_vacancies("")

    assert res._connect_to_api() == part_answer__connect_to_api
    assert res.vacancies == part_answer_get_vacancies


@patch("requests.get")
def test__connect_to_api(mock_get, arguments_for_init, part_answer__connect_to_api):
    res = HHApi(*arguments_for_init)
    mock_get.return_value.json.return_value = part_answer__connect_to_api
    mock_get.return_value.status_code = 400

    assert res._connect_to_api() is None
