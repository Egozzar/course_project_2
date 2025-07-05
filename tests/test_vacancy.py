from src.vacancy import Vacancy


def test_vacancy_init(arg_init_vacancy):
    result = Vacancy(*arg_init_vacancy)

    assert result.salary_min == 100000
    assert result.address == "Москва, Новоданиловская набережная, 12"
    assert result.url == "https://api.hh.ru/vacancies/121933473?host=hh.ru"
    assert result.requirement == "Опыт коммерческой разработки на Python от 1 года."
    assert result.profession == "Программист, разработчик"


def test_vacancy_init_wrong(arg_init_vacancy_wrong):
    result = Vacancy(*arg_init_vacancy_wrong)

    assert hasattr(result, "_Vacancy__salary_min") is False
    assert hasattr(result, "_Vacancy__address") is False
    assert hasattr(result, "_Vacancy__url") is False
    assert hasattr(result, "_Vacancy__requirement") is False
    assert hasattr(result, "_Vacancy__profession") is False


def test_gt__(arg_init_vacancy, arg_gt_vacancy):
    result1 = Vacancy(*arg_init_vacancy)
    result2 = Vacancy(*arg_gt_vacancy)

    assert result2 > result1
    assert result1 < result2
    assert result1 > 2000


def test_gt__wrong(capsys, arg_init_vacancy, arg_gt_vacancy):
    result = Vacancy(*arg_init_vacancy)
    check = result > "12345"

    captured = capsys.readouterr()
    assert captured.out[:-1] == "Несравнимые объекты"
    assert check is False


def test_create_vacancy(dict_for_create_vacancy):
    result = Vacancy.create_vacancy(dict_for_create_vacancy)

    assert result.salary_min == 150000
    assert result.address == "Москва, проспект Андропова, 22"
    assert result.url == "https://api.hh.ru/vacancies/121994575?host=hh.ru"
    assert result.requirement == "Высшее или среднее профессиональное образование"
    assert result.profession == "Программист, разработчик"


def test_to_json(arg_init_vacancy, dict_for_json):
    instance = Vacancy(*arg_init_vacancy)

    assert instance.to_json() == dict_for_json
