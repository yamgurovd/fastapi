
from datetime import date
from faker import Faker
from typing import Any


def generate_profession_name(fake: Faker = Faker("ru-RU"),
                             is_added_symbols: bool = False,
                             generate_symbols: Any = None) -> date | Any:
    """

    :param generate_symbols: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует Название провефесии + дополнительные символы(если необходимо) example - Повар
    """
    if is_added_symbols:
        return fake.job() + ''.join(generate_symbols)
    else:
        return fake.job()


def generate_company_name(fake: Faker = Faker("ru-RU"),
                          is_added_symbols: bool = False,
                          generate_symbols: Any = None) -> date | Any:
    """

    :param generate_symbols: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует Название провефесии + дополнительные символы(если необходимо) example - Повар
    """
    if is_added_symbols:
        return fake.company() + ''.join(generate_symbols)
    else:
        return fake.company()
