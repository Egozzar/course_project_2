from typing import Final
import os

# Универсальный адрес корня проекта
ROOT_PATH: Final[str] = os.path.dirname(__file__)

# Адрес API hh.ru.
url_api: str = "https://api.hh.ru/vacancies"

# Заголовки запроса к API hh.ru
headers = {"User-Agent": "HH-User-Agent"}

# Параметры запроса к API hh.ru
params: dict = {
    "text":"", # Поисковый запрос
    "per_page": 100, # Количество вакансий на странице
    "page": 0, # Номер страницы
    "period": 14, # Количество дней, в пределах которых нужно найти вакансии
    "area": 1 # код региона, по которому осуществляется поиск (1 — Москва)
}

# функция для создания пустого словаря
create_dict: callable = lambda: {} # pragma: no cover


# Аргументы для функции получения вакансий с hh.ru
arguments: list = [
    url_api,
    headers,
    params
]

#pytest --cov=src --cov-report=html -генерация отчета о покрытии в HTML-формате
