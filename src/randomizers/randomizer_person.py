from faker import Faker
import random
from typing import Any


def generate_name_male(fake: Faker = Faker("ru-RU"),
                       is_added_symbols: bool = False,
                       generate_symbol: Any = None) -> str:
    """

    :param generate_symbol: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует Мужское ФИО + дополнительные символы(если необходимо) example - Иосиф Алексеевич Блохин
    """
    if is_added_symbols:
        return fake.name_male() + ''.join(generate_symbol)
    else:
        return fake.name_male()


def generate_name_female(fake: Faker = Faker("ru-RU"),
                         is_added_symbols: bool = False,
                         generate_symbol: Any = None) -> str:
    """

    :param generate_symbol: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует Женское ФИО + дополнительные символы(если необходимо) example - Элеонора Петровна Белякова
    """
    if is_added_symbols:
        return fake.name_female() + ''.join(generate_symbol)
    else:
        return fake.name_female()


def generate_first_name_male(fake: Faker = Faker("ru-RU"),
                             is_added_symbols: bool = False,
                             generate_symbol: Any = None) -> str:
    """

    :param generate_symbol: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует мужское имя + дополнительные символы(если необходимо) example - Ираклий
    """
    if is_added_symbols:
        return fake.first_name_male() + ''.join(generate_symbol)
    else:
        return fake.first_name_male()


def generate_first_name_female(fake: Faker = Faker("ru-RU"),
                               is_added_symbols: bool = False,
                               generate_symbol: Any = None) -> str:
    """

    :param generate_symbol: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует женское имя + дополнительные символы(если необходимо) example - Анна
    """
    if is_added_symbols:
        return fake.first_name_female() + ''.join(generate_symbol)
    else:
        return fake.first_name_female()


def generate_last_name_male(fake: Faker = Faker("ru-RU"),
                            is_added_symbols: bool = False,
                            generate_symbol: Any = None) -> str:
    """

    :param generate_symbol: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует мужскую фамилию + дополнительные символы(если необходимо) example - Морозов
    """
    if is_added_symbols:
        return fake.last_name_male() + ''.join(generate_symbol)
    else:
        return fake.last_name_male()


def generate_last_name_female(fake: Faker = Faker("ru-RU"),
                              is_added_symbols: bool = False,
                              generate_symbol: Any = None) -> str:
    """

    :param generate_symbol: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует женскую фамилию + дополнительные символы(если необходимо) example - Бобылева
    """
    if is_added_symbols:
        return fake.last_name_female() + ''.join(generate_symbol)
    else:
        return fake.last_name_female()


def generate_middle_name_male(fake: Faker = Faker("ru-RU"),
                              is_added_symbols: bool = False,
                              generate_symbol: Any = None) -> str:
    """

    :param generate_symbol: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует мужское отчество + дополнительные символы(если необходимо) example - Изотович
    """
    if is_added_symbols:
        return fake.middle_name_male() + ''.join(generate_symbol)
    else:
        return fake.middle_name_male()


def generate_middle_name_female(fake: Faker = Faker("ru-RU"),
                                is_added_symbols: bool = False,
                                generate_symbol: Any = None) -> str:
    """

    :param generate_symbol: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует мужское отчество + дополнительные символы(если необходимо) example - Захаровна
    """
    if is_added_symbols:
        return fake.middle_name_female() + ''.join(generate_symbol)
    else:
        return fake.middle_name_female()