from abc import ABC, abstractmethod
from typing import Optional


class AbstractForAPI(ABC):
    """
    Абстрактный класс-шаблон для создания необходимой структуры
    классов-наследников, получающих информацию на свои запросы
    с внешних сервисов
    """

    @abstractmethod
    def _connect_to_api(self) -> Optional[list]: # pragma: no cover
        """
        Метод для подключения к API внешнего сервиса
        :return:(Optional[Response]) ответ внешнего сервиса
        """
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str) -> None: # pragma: no cover
        """
        Метод для получения вакансий с внешнего сервиса
        :param keyword:(str) ключевое слово для поиска вакансий
        :return:(None)
        """
        pass
    