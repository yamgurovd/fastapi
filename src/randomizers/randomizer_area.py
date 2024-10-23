from faker import Faker
import random
from typing import Any


def generate_address(fake: Faker = Faker("ru-RU"),
                     is_added_symbols: bool = False,
                     generate_symbols: Any = None) -> str:
    """

    :param generate_symbols: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует полный адрес + дополнительные символы(если необходимо) example - . Добрянка, ш. Красина, д. 8, 885431
    """
    if is_added_symbols:
        return fake.address() + ''.join(generate_symbols)
    else:
        return fake.address()


def generate_street_address(fake: Faker = Faker("ru-RU"),
                            is_added_symbols: bool = False,
                            generate_symbols: Any = None) -> str:
    """

    :param generate_symbols: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует адрес + дополнительные символы(если необходимо) example - . ш. Коммунаров, д. 746 к. 2
    """
    if is_added_symbols:
        return fake.street_address() + ''.join(generate_symbols)
    else:
        return fake.mac_address()


def generate_region(fake: Faker = Faker("ru-RU"),
                    is_added_symbols: bool = False,
                    generate_symbols: Any = None) -> str:
    """

    :param generate_symbols: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует регион + дополнительные символы(если необходимо) example - . обл. Астраханская
    """
    if is_added_symbols:
        return fake.region() + ''.join(generate_symbols)
    else:
        return fake.region()


def generate_city(fake: Faker = Faker("ru-RU"),
                  is_added_symbols: bool = False,
                  generate_symbols: Any = None) -> str:
    """

    :param generate_symbols: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует город + дополнительные символы(если необходимо) example - . ст. Ахтубинск
    """
    if is_added_symbols:
        return fake.city() + ''.join(generate_symbols)
    else:
        return fake.city()


def generate_latitude(fake: Faker = Faker("ru-RU"),
                      is_added_symbols: bool = False,
                      generate_symbols: Any = None) -> str:
    """

    :param generate_symbols: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует широту + дополнительные символы(если необходимо) example - . 34.749059
    """
    if is_added_symbols:
        return fake.latitude() + ''.join(generate_symbols)
    else:
        return fake.latitude()


def generate_city_name(fake: Faker = Faker("ru-RU"),
                       is_added_symbols: bool = False,
                       generate_symbols: Any = None) -> str:
    """

    :param generate_symbols: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует город + дополнительные символы(если необходимо) example - Стерлитамак
    """
    if is_added_symbols:
        return fake.city_name() + ''.join(generate_symbols)
    else:
        return fake.city_name()


def generate_settlement(fake: Faker = Faker("ru-RU"),
                        is_added_symbols: bool = False,
                        generate_symbols: Any = None) -> str:
    """

    :param generate_symbols: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует место проживания + дополнительные символы(если необходимо) example - Арзамас
    """
    if is_added_symbols:
        return fake.settlement() + ''.join(generate_symbols)
    else:
        return fake.settlement()


def generate_street_address_with_county(fake: Faker = Faker("ru-RU"),
                                        is_added_symbols: bool = False,
                                        generate_symbols: Any = None) -> str:
    """

    :param generate_symbols: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует Полный адрес страну включая + дополнительные символы(если необходимо) example - Арзамас
    """
    if is_added_symbols:
        return fake.street_address_with_county() + ''.join(generate_symbols)
    else:
        return fake.street_address_with_county()