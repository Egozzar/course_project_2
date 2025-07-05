from abc import ABC, abstractmethod
from typing import Any


class AbstractHandler(ABC):
    """
    Абстрактный класс-шаблон для создания необходимой структуры
    классов-наследников, занимающихся обработкой информации в файлах
    """

    @abstractmethod
    def adding_vacancies(self, instances_lst: list, keyword: str) -> None:  # pragma: no cover
        """
        Метод добавления вакансий в файл
        :param instances_lst: (list) список вакансий
        :param keyword: (str) ключевая часть названия файла
        """
        pass

    @abstractmethod
    def getting_data(self, name: str) -> tuple:  # pragma: no cover
        """
        Метод получения данных из файла
        :param name: (str) имя файла
        :return: (tuple) кортеж (список вакансий, если он есть в файле; и путь к файлу)
        """
        pass

    @abstractmethod
    def deleting_information(self, new_coll: Any, old_coll: list) -> list:  # pragma: no cover
        """
        Метод удаления вакансии из файла вследствие неактуальности
        :param new_coll: (Any) новая коллекция вакансий для дозаписи в файл
        :param old_coll: (list) коллекция вакансий, записанная в файле
        return: (list) список вакансий после преобразования
        """
        pass
