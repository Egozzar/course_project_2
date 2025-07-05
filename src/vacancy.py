from __future__ import annotations

import re
from typing import Any, Optional, Union

from src.file_handler import FileHandler


class Vacancy:
    """
    Класс для создания объекта вакансии
    """

    __slots__ = ("__url", "__profession", "__requirement", "__salary_min", "__address")

    def __init__(self, url: str, profession: str, requirement: str, salary_min: int, address: str) -> None:
        """
        Метод инициализирует новый экземпляр класса
        :param url: (str) ссылка на вакансию
        :param profession: (str) название профессии
        :param requirement: (str) требования
        :param salary_min: (int) минимальная месячная зарплата
        :param address: (str) адрес места работы
        """

        self.url = url
        self.profession = profession
        self.requirement = requirement
        self.salary_min = salary_min
        self.address = address

    @classmethod
    def __verify_url(cls, url: str) -> bool:
        """
        Метод для проверки ссылки на вакансию
        :param url: (str) проверяемая ссылка
        :return: (bool) результат проверки
        """
        return url.startswith("https://api.hh.ru/vacancies")

    @property
    def url(self) -> str:
        """
        Геттер приватного свойства ссылки на вакансию
        :return: (str) ссылка
        """
        return self.__url

    @url.setter
    def url(self, string: str) -> None:
        """
        Сеттер приватного свойства ссылки на вакансию
        :param string: (str) принимаемая ссылка
        """
        if self.__verify_url(string):
            self.__url = string

    @classmethod
    def __verify_prof(cls, prof: str) -> bool:
        """
        Метод для проверки названия предлагаемой профессии
        :param prof:(str) заявленная профессия
        :return: (bool) результат проверки
        """
        pattern_dev = re.compile("Программист")
        pattern_test = re.compile("Тестировщик")

        return bool(pattern_dev.search(prof)) or bool(pattern_test.search(prof))

    @property
    def profession(self) -> str:
        """
        Геттер приватного свойства названия профессии
        :return: (str) профессия
        """
        return self.__profession

    @profession.setter
    def profession(self, string: str) -> None:
        """
        Сеттер приватного свойства названия профессии
        :param string: принимаемое название по вакансии
        """
        if self.__verify_prof(string):
            self.__profession = string

    @classmethod
    def __verify_requirement(cls, requirement: str) -> bool:
        """
        Метод для проверки требований по вакансии
        :param requirement: (str) требования по вакансии
        :return: (bool) результат проверки
        """

        return bool(requirement)

    @property
    def requirement(self) -> str:
        """
        Геттер приватного свойства требований по вакансии
        :return: (str) требования
        """
        return self.__requirement

    @requirement.setter
    def requirement(self, string: str) -> None:
        """
        Сеттер приватного свойства требований по вакансии
        :param string: принимаемые требования
        """
        if self.__verify_requirement(string):
            self.__requirement = string

    @classmethod
    def __verify_salary_min(cls, sal: int) -> bool:
        """
        Метод для проверки минимальной зарплаты
        :param sal: (int) минимальная зарплата по вакансии
        :return: (bool) результат проверки
        """
        if sal is None or sal < 70000:
            return False
        else:
            return True

    @property
    def salary_min(self) -> int:
        """
        Геттер приватного свойства минимальной зарплаты
        :return: (int) минимальная зарплата
        """
        return self.__salary_min

    @salary_min.setter
    def salary_min(self, value: int) -> None:
        """
        Сеттер приватного свойства минимальной зарплаты
        :param value: (int) принимаемая минимальная зарплата по вакансии
        """
        if self.__verify_salary_min(value):
            self.__salary_min = value

    @classmethod
    def __verify_address(cls, string: str) -> bool:
        """
        Метод для проверки наличия адреса работы
        :param string: (str) адрес места работы по вакансии
        :return: (bool) результат проверки
        """
        if not string:
            return False
        else:
            return True

    @property
    def address(self) -> str:
        """
        Геттер приватного свойства адреса места работы
        :return: (str) адрес работы
        """
        return self.__address

    @address.setter
    def address(self, string: str) -> None:
        """
        Сеттер приватного свойства адреса места работы
        :param string: (str) принимаемый адрес по вакансии
        """
        if self.__verify_address(string):
            self.__address = string

    @classmethod
    def __verify_vacancies(cls, other: Any) -> Any:
        """
        Метод для проверки типа сравниваемого объекта
        :param other: (Any) принимаемый объект для проверки
        :return: (Any) результат проверки
        """
        if not isinstance(other, (int, Vacancy)):
            return False

        return other.salary_min if isinstance(other, Vacancy) else other

    def __gt__(self, other: Union[Vacancy, int]) -> Any:
        """
        Метод сравнения на "больше" между экземплярами класса
        :param other: Union[Vacancy, int] принимаемый объект для сравнения
        :return: (Any) результат сравнения
        """
        obj = self.__verify_vacancies(other)

        if obj:
            return self.salary_min > obj
        else:
            print("Несравнимые объекты")
            return False

    def __lt__(self, other: Union[Vacancy, int]) -> Any:
        """
        Метод сравнения на "меньше" между экземплярами класса
        :param other: Union[Vacancy, int] принимаемый объект для сравнения
        :return: (Any) результат сравнения
        """
        obj = self.__verify_vacancies(other)

        if obj:
            return self.salary_min < obj
        else:
            print("Несравнимые объекты")
            return False

    @classmethod
    def create_vacancy(cls, vacancy_dict: dict) -> Optional[Vacancy]:
        """
        Метод создания экземпляра класса Vacancy из полученной вакансии
        :param vacancy_dict: (dict) полученная на входе вакансия
        :return: Optional[Vacancy] созданный объект либо None, если вакансия
        не соответствует необходимым требованиям
        """

        # Получение аргументов (5шт) для создания экземпляра класса. Сначала промежуточное
        # значение, на случай если нужного ключа нет в словаре, затем исключаем значение None
        address_ = vacancy_dict.get("address", {})
        address = address_.get("raw", "") if address_ else ""

        url_ = vacancy_dict.get("url", "")
        url = url_ if url_ else ""

        profession_ = vacancy_dict.get("professional_roles", [{}])
        profession = profession_[0].get("name", "") if profession_ else ""

        requirement_ = vacancy_dict.get("snippet", {})
        requirement = requirement_.get("requirement", "") if requirement_ else ""

        salary_min_ = vacancy_dict.get("salary", {})
        salary_min2_ = salary_min_.get("from", 0) if salary_min_ else 0
        salary_min = salary_min2_ or (salary_min_.get("to", 0) if salary_min_ else 0)

        vacancy = cls(url, profession, requirement, salary_min, address)

        if cls.checking_attributes(vacancy):

            return vacancy
        return None

    @staticmethod
    def checking_attributes(instance: Vacancy) -> bool:
        """
        Метод проверки соответствия количества атрибутов экземпляра класса
        заявленному в __slots__
        :param instance: (Vacancy) экземпляр класса для проверки
        :return: (bool) результат проверки
        """
        attributes = []

        for attr in instance.__slots__:
            if attr[:2] == "__":
                attr = f"_{instance.__class__.__name__}{attr}"
            try:
                attributes.append(getattr(instance, attr))
            except AttributeError:
                pass

        return True if len(attributes) == len(instance.__slots__) else False

    @classmethod
    def create_vacancies(cls, working_dict: dict) -> Union[list, str]:
        """
        Метод создания списка отфильтрованных вакансий
        :param working_dict: (dict) словарь "необработанных" вакансий
        :return: (Union[list, str]) список вакансий, соответствующих всем требованиям
        """
        # Извлекаем ключ и значение чернового списка
        keyword = [*working_dict][0]
        vacancies_lst = working_dict[keyword]

        if not vacancies_lst:
            return "Вакансий по этому запросу пока нет"

        # Генерируем результирующий список вакансий
        selected_vacancies = [cls.create_vacancy(elem) for elem in vacancies_lst if cls.create_vacancy(elem)]

        # Передаём данные для записи в json-файл
        reporter = FileHandler()
        reporter.adding_vacancies(selected_vacancies, keyword)

        # Выводим новые вакансии, записанные в файл
        if selected_vacancies:
            return selected_vacancies
        else:
            file_name = f"reports/on_request_{keyword}.json" if keyword else "on_empty_request.json"
            answer = (
                f"А вот ничего нового по этой теме не пишут.\n"
                f"Всё, что в файле '{file_name}' - всё самое свежее.\n"
                f"Пишите письма!.."
            )

            return answer

    def to_json(self) -> dict:
        """
        Метод представления экземпляра класса для преобразования
        его в формат json
        :return: (dict) словарь для сериализации
        """
        return {
            "url": self.url,
            "profession": self.profession,
            "requirement": self.requirement,
            "salary_min": self.salary_min,
            "address": self.address,
        }

    # Для отображения экземпляра объекта в формате строки сначала выбрал __str__,
    # но он почему-то не отработал, а вот __repr__ вполне себе зашёл. Почему-то.
    def __repr__(self) -> str:
        """
        Метод отображения экземпляра объекта в формате строки
        """
        return f"""____________________
 'url': {self.url},
 'profession': {self.profession},
 'requirement': {self.requirement},
 'salary_min': {self.salary_min},
 'address': {self.address}
 """
