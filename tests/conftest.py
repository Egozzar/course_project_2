import pytest


@pytest.fixture
def arguments_for_init():
    return [
        dict(),
        "https://api.hh.ru/vacancies",
        {"User-Agent": "HH-User-Agent"},
        {"per_page": 1, "text": "", "page": 0},
    ]


@pytest.fixture
def arguments_for_init_wrong():
    return [
        {"a": 1},
        "https://api.hh.ru/vacancies",
        {"User-Agent": "HH-User-Agent"},
        {"per_page": 1, "text": "", "page": 0},
    ]


@pytest.fixture
def part_answer__connect_to_api():
    return {
        "items": [
            {
                "salary": {"currency": "RUR", "from": 80001, "gross": False, "to": 180000},
                "salary_range": {
                    "currency": "RUR",
                    "frequency": None,
                    "from": 80001,
                    "gross": False,
                    "mode": {"id": "MONTH", "name": "За\xa0месяц"},
                    "to": 180000,
                },
            }
        ]
    }


@pytest.fixture
def part_answer_get_vacancies():
    return {
        "": [
            {
                "salary": {"currency": "RUR", "from": 80001, "gross": False, "to": 180000},
                "salary_range": {
                    "currency": "RUR",
                    "frequency": None,
                    "from": 80001,
                    "gross": False,
                    "mode": {"id": "MONTH", "name": "За\xa0месяц"},
                    "to": 180000,
                },
            }
        ]
        * 5
    }


@pytest.fixture
def arg_init_vacancy():
    return [
        "https://api.hh.ru/vacancies/121933473?host=hh.ru",
        "Программист, разработчик",
        "Опыт коммерческой разработки на Python от 1 года.",
        100000,
        "Москва, Новоданиловская набережная, 12",
    ]


@pytest.fixture
def arg_gt_vacancy():
    return [
        "https://api.hh.ru/vacancies/121933473?host=hh.ru",
        "Программист, разработчик",
        "Опыт коммерческой разработки на Python от 1 года.",
        150000,
        "Москва, Новоданиловская набережная, 12",
    ]


@pytest.fixture
def arg_init_vacancy_wrong():
    return ["https://api.hh.ru/vacanc", "Менеджер", "", 10000, ""]


@pytest.fixture
def dict_for_create_vacancy():
    return {
        "address": {"raw": "Москва, проспект Андропова, 22"},
        "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
        "salary": {"currency": "RUR", "from": None, "gross": False, "to": 150000},
        "snippet": {"requirement": "Высшее или среднее профессиональное образование"},
        "url": "https://api.hh.ru/vacancies/121994575?host=hh.ru",
    }


@pytest.fixture
def arg_init_vacancy_triple():
    return [
        "https://api.hh.ru/vacancies/123456789?host=hh.ru",
        "Программист, разработчик",
        "Опыт коммерческой разработки на Python от 1 года.",
        100000,
        "Москва, Новоданиловская набережная, 12",
    ]


@pytest.fixture
def note_from_file():
    return [
        {
            "address": "Москва, Новоданиловская набережная, 12",
            "profession": "Программист, разработчик",
            "requirement": "Опыт коммерческой разработки на Python от 1 года.",
            "salary_min": 100000,
            "url": "https://api.hh.ru/vacancies/121933473?host=hh.ru",
        }
    ]


@pytest.fixture
def dict_for_json():
    return {
        "address": "Москва, Новоданиловская набережная, 12",
        "profession": "Программист, разработчик",
        "requirement": "Опыт коммерческой разработки на Python от 1 года.",
        "salary_min": 100000,
        "url": "https://api.hh.ru/vacancies/121933473?host=hh.ru",
    }
