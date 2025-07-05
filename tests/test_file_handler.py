import json
import os

from config import ROOT_PATH
from src.file_handler import FileHandler
from src.vacancy import Vacancy


def test_file_handler_init():
    instance = FileHandler()

    assert instance.file_name == "on_empty_request.json"


def test_adding_vacancies(arg_init_vacancy, note_from_file):
    vacancy = Vacancy(*arg_init_vacancy)
    handler = FileHandler()
    test_path = os.path.join(ROOT_PATH, "reports", "on_request_test.json")
    handler.adding_vacancies([vacancy], "test")

    assert os.path.exists(test_path)

    with open(test_path, encoding="UTF-8") as file:
        result = json.load(file)

    assert result == note_from_file


def test_adding_vacancies_double(arg_init_vacancy, arg_init_vacancy_triple):
    vacancy1 = Vacancy(*arg_init_vacancy_triple)
    vacancy2 = Vacancy(*arg_init_vacancy)
    handler = FileHandler()
    test_path = os.path.join(ROOT_PATH, "reports", "on_request_test.json")
    handler.adding_vacancies([vacancy1, vacancy2], "test")

    with open(test_path, encoding="UTF-8") as file:
        res = json.load(file)

    assert len(res) == 2
