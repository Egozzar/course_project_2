from functools import reduce
from time import sleep
from typing import Any

from config import create_dict, headers, params, url_api
from src.hh_api import HHApi
from src.vacancy import Vacancy


def main() -> None:
    """
    Функция формирует основную логику проекта и связывает функциональности между собой.
    :return: None
    """
    # Объявление и получение локальных переменных
    user_digit: str  # выбранный пункт меню
    user_topic: str  # указанная пользователем тема запроса
    favorit: Any  # вакансия с наибольшей минимальной зарплатой
    farewell_message: str = "Пока!"
    encouraging_message: str = "Жди..."
    good_advice: str = "Думай..."
    beautiful_separator: tuple = ("_" * 20, "\n")

    # Приветствие
    print(
        "Привет. Сегодня будем искать вакансии по профессиям 'Программист' и 'Тестировщик',\n"
        "и искать мы их будем в городе Москва!"
    )

    # Игра
    print(*beautiful_separator)
    sleep(1)
    menu_lst: list = ["надоело", "Ruby", "PHP", "JavaScript", "C++", "Python"]

    print(
        "Выбери номер волшебного слова:\n"
        "1 - Ruby\n"
        "2 - PHP\n"
        "3 - JavaScript\n"
        "4 - C++\n"
        "5 - Python\n"
        "0 - надоело\n"
        "Любая другая цифра или буква(ы) будет расцениваться как провокация (пустой запрос)\n"
        "Можешь вообще ничего не писать - всё равно что-то да найдётся."
    )

    user_digit = input().strip()

    if user_digit == "0":
        print(farewell_message)

        return

    if user_digit in ("1", "2", "3", "4", "5"):
        user_topic = menu_lst[int(user_digit)]
    else:
        user_topic = ""

    print(*beautiful_separator)
    print(encouraging_message)

    # Создание экземпляра поисковика с пользовательскими настройками
    search_agent = HHApi(create_dict(), url_api, headers, params)

    # Получение вакансий с внешнего ресурса
    search_agent.get_vacancies(user_topic)

    # Отбираем из общей массы предложения, удовлетворяющие нашим требованиям,
    # создаём экземпляры вакансий, дописываем новые в файл, удаляем из файла неактуальные
    # и показываем пользователю, если есть что-то свежее

    grand_result = Vacancy.create_vacancies(search_agent.vacancies)
    print(grand_result)
    print(*beautiful_separator)

    if isinstance(grand_result, list):
        print(
            f"Нужны новые рабы на галеры аж {len(grand_result)} шт. Всё уже запротоколировано\n"
            f"куда надо (см. в папке 'reports' по своему запросу)"
        )

        print(*beautiful_separator)
        print("А сейчас узнаем, что обещает самый щедрый белый господин")
        sleep(3)  # барабанная дробь

        favorit = reduce(lambda res, elem: elem if elem > res else res, grand_result)
        print(*beautiful_separator)

        print(f"Аж цельных {favorit.salary_min} тугриков!!!")

        print(*beautiful_separator)
        print(good_advice)


if __name__ == "__main__":
    main()
