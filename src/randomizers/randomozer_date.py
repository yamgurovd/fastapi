from datetime import datetime, date
from faker import Faker
import random
from typing import Any


def generate_date(fake: Faker = Faker("ru-RU"),
                  is_added_symbols: bool = False,
                  generate_symbol: Any = None) -> Any:
    """

    :param generate_symbol: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: енерирует фейковую дату в заданном промежутке example - 2023-01-01
    """

    start_dt = datetime(2010, 1, 1)
    end_dt = datetime(2030, 1, 1)

    if is_added_symbols:
        return fake.date_between() + ''.join(generate_symbol)
    else:
        return fake.date_between(start_date=start_dt, end_date=end_dt)


def generate_date_this_year(fake: Faker = Faker("ru-RU"),
                            is_added_symbols: bool = False,
                            generate_symbol: Any = None) -> date | Any:
    """

    :param generate_symbol: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует дату в текущем года + дополнительные символы(если необходимо) example - 2024-04-21
    """
    if is_added_symbols:
        return fake.date_this_year() + ''.join(generate_symbol)
    else:
        return fake.date_this_year()


def generate_date_time(fake: Faker = Faker("ru-RU"),
                       is_added_symbols: bool = False,
                       generate_symbol: Any = None) -> datetime:
    """

    :param generate_symbol: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует дату + время - дополнительные символы(если необходимо) example - 1993-10-07 05:16:44.321030
    """
    if is_added_symbols:
        return fake.date_time() + ''.join(generate_symbol)
    else:
        return fake.date_time()


def generate_future_date(fake: Faker = Faker("ru-RU"),
                         is_added_symbols: bool = False,
                         generate_symbol: Any = None) -> datetime | Any:
    """

    :param generate_symbol: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует дату в будущем - дополнительные символы(если необходимо) example - 2024-08-14
    """
    if is_added_symbols:
        return fake.date_time() + ''.join(generate_symbol)
    else:
        return fake.date_time()


def generate_date_between(minimum_age: int,
                          maximum_age: int,
                          fake: Faker = Faker("ru-RU"),
                          is_added_symbols: bool = False,
                          generate_symbol: Any = None) -> date | Any:
    """

    :param maximum_age: Максимальная граница
    :param minimum_age:
    :param generate_symbol: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует дату в будущем - дополнительные символы(если необходимо) example - 2024-08-14
    """
    if is_added_symbols:
        return fake.date_of_birth(minimum_age=minimum_age, maximum_age=maximum_age) + ''.join(generate_symbol)
    else:
        return fake.date_of_birth(minimum_age=minimum_age, maximum_age=maximum_age)