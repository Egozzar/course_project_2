from typing import Any

import requests

from src.abstract_for_api import AbstractForAPI


class DescriptArg:
    """
    Класс для создания дескрипторов данных (data descriptor)
    """

    @classmethod
    def verify_arg(cls, arg: Any) -> bool:
        """
        Метод проверки аргумента, присваиваемого защищённому аргументу класса
        :param arg: (Any) аргумент, передаваемый в сеттер
        :return: (bool) результат проверки аргумента
        """
        match arg:
            # минимальный состав params по ТЗ
            case {"per_page": int(), "text": str()}:
                return True
            # наличие какого-нибудь адреса
            case str(url) if url:
                return True
            # наличие headers
            case {"User-Agent": user_agent}:
                return True
            # наличие пустого словаря
            case dict(vacancies) if not vacancies:
                return True
            case _:  # wildcard
                return False

    def __set_name__(self, owner: Any, name: str) -> None:
        """
        Метод создания имени защищённого атрибута экземпляра класса
        :param owner: (Any) ссылка на класс, в котором создаются дескрипторы
        :param name: (str) имя аргумента для преобразования
        :return: (None)
        """
        self.name = "_" + name

    def __get__(self, instance: Any, owner: Any) -> Any:
        """
        Метод возвращает значение защищённого атрибута экземпляра класса
        :param instance:(Any) ссылка на экземпляр класса, из которого
        вызывается дескриптор
        :param owner: (Any) ссылка на класс, в котором создаётся дескриптор
        :return: (Any) значение атрибута
        """
        return getattr(instance, self.name)

    def __set__(self, instance: Any, value: Any) -> None:
        """
        Метод устанавливает значение защищённому атрибуту экземпляра класса
        :param instance: (Any) ссылка на экземпляр класса, из которого
        вызывается дескриптор
        :param value: (Any) значение, передаваемое защищённому атрибуту экземпляра класса
        :return: (None)
        """
        if self.verify_arg(value):
            setattr(instance, self.name, value)


class HHApi(AbstractForAPI):
    """
    Класс, наследуемый от абстрактного класса, для работы с платформой hh.ru.
    Экземпляры класса подключаются к API и получают вакансии.
    """

    # Создание аргументов класса(дескрипторов), необходимых
    # для формирования аргументов экземпляра класса
    url_api = DescriptArg()
    headers = DescriptArg()
    params = DescriptArg()
    vacancies = DescriptArg()

    def __init__(self, vacancies_dict: dict, url: str, headers_dict: dict, params_dict: dict) -> None:
        """
        Метод инициализирует новый экземпляр класса
        :param vacancies_dict: (dict) пустой словарь для сбора вакансий
        :param url: (str) адрес внешнего сервиса
        :param headers_dict: (dict) словарь с заголовками для запроса
        :param params_dict: (dict) словарь с параметрами для запроса
        """
        self.url_api = url
        self.headers = headers_dict
        self.params = params_dict
        self.vacancies = vacancies_dict

    def _connect_to_api(self) -> Any:
        """
        Метод для подключения к API внешнего сервиса
        :return:(Any) ответ внешнего сервиса
        """
        response = requests.get(self.url_api, headers=self.headers, params=self.params)
        status_code = response.status_code

        if status_code == 200:

            return response.json()
        return None

    def get_vacancies(self, keyword: str = "") -> None:
        """
        Метод получения данных отправляет запрос на API hh.ru для получения данных о вакансиях по ключевому слову.
        Вносит данные ответа в формате словарей в список (атрибут экземпляра)
        :param keyword: (str) ключевое слово для поиска
        :return: (None)
        """
        self.params["text"] = keyword

        while self.params["page"] != 5:
            result = self._connect_to_api()

            if result:
                vacancies_lst = self.vacancies.get(keyword, [])
                vacancies_lst.extend(result["items"])
                self.vacancies[keyword] = vacancies_lst

            self.params["page"] += 1
