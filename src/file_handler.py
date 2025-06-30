import json
import os
from typing import Any, Callable, Optional

from config import ROOT_PATH
from src.abstract_handler import AbstractHandler


class FileHandler(AbstractHandler):
    """
    Класс для создания обработчиков информации в файлах
    """

    def __init__(self) -> None:
        """
        Метод инициализирует экземпляр класса
        """
        self.file_name = "on_empty_request.json"

    @property
    def file_name(self) -> str:
        """
        Метод-геттер возвращает значение приватного атрибута
        :return: (str) название файла
        """
        return self.__file_name

    @file_name.setter
    def file_name(self, string: str) -> None:
        """
        Метод-сеттер присваивает значение приватному атрибуту
        :param string: (str) название файла
        """
        if self.verify_name(string):
            self.__file_name = string
        else:
            self.__file_name = "on_empty_request.json"

    @classmethod
    def verify_name(cls, string: str) -> bool:
        """
        Метод проверяет введённое название файла на соответствие
        необходимым требованиям
        :param string: (str) проверяемая строка
        :return: (bool) результат проверки
        """
        if string == "on_request_.json":
            return False
        return True

    def adding_vacancies(self, instances: list, keyword: str) -> None:
        """
        Метод добавления вакансий в файл
        :param instances: (list) список с вакансиями
        :param keyword: (str) ключевая часть названия файла
        """
        util: Optional[Callable] = None  # параметр-функция для сериализации экземпляров класса
        collection: Any = []  # данные, передаваемые при сериализации для записи в файл

        if not instances:
            return

        self.file_name = f"on_request_{keyword}.json"

        vacancies, reports_path = self.getting_data(self.file_name)

        if vacancies:
            vacancies_ = self.deleting_information(instances, vacancies)
            if vacancies_:
                vacancies_urls = [dct["url"] for dct in vacancies_]

                for indx in range(len(instances))[::-1]:
                    if instances[indx].url in vacancies_urls:
                        del instances[indx]
                    else:
                        vacancies_.append(instances[indx].to_json())

                collection = vacancies_
            else:
                collection = instances
                util = lambda obj: obj.to_json()
        else:
            collection = instances
            util = lambda obj: obj.to_json()

        with open(reports_path, "w", encoding="UTF-8") as file:
            json.dump(collection, file, indent=4, ensure_ascii=False, default=util)

    def getting_data(self, name: str) -> tuple:
        """
        Метод получения данных из файла
        :param name: (str) имя файла
        :return: (tuple) кортеж (список вакансий, если он есть в файле; и путь к файлу)
        """
        reports_path = os.path.join(ROOT_PATH, "reports", name)

        if not os.path.exists(reports_path):
            return [], reports_path

        with open(reports_path, encoding="UTF-8") as file:
            vacancies = json.load(file)

        return vacancies, reports_path

    def deleting_information(self, new_coll: Any, old_coll: list) -> list:
        """
        Метод удаления вакансии из файла вследствие неактуальности
        :param new_coll: (Any) новая коллекция вакансий для дозаписи в файл
        :param old_coll: (list) коллекция вакансий, записанная в файле
        return: (list) список вакансий после преобразования
        """
        new_coll_urls = [inst.url for inst in new_coll]

        for indx in range(len(old_coll))[::-1]:
            if old_coll[indx]["url"] not in new_coll_urls:
                del old_coll[indx]

        return old_coll
