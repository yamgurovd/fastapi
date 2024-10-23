from datetime import date
from faker import Faker
import random
from typing import Any


def generate_email(fake: Faker = Faker("ru-RU"),
                   is_added_symbols: bool = False,
                   generate_symbol: Any = None) -> date | Any:
    """

    :param generate_symbol: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует Email + дополнительные символы(если необходимо) example - melanie91@example.org
    """
    if is_added_symbols:
        return fake.email() + ''.join(generate_symbol)
    else:
        return fake.email()


def generate_free_email_domain(fake: Faker = Faker("ru-RU"),
                               is_added_symbols: bool = False,
                               generate_symbol: Any = None) -> date | Any:
    """

    :param generate_symbol: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует домен почты + дополнительные символы(если необходимо) example - hotmail.com
    """
    if is_added_symbols:
        return fake.free_email_domain() + ''.join(generate_symbol)
    else:
        return fake.free_email_domain()


def generate_company_email(fake: Faker = Faker("ru-RU"),
                           is_added_symbols: bool = False,
                           generate_symbol: Any = None) -> date | Any:
    """

    :param generate_symbol: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует корпоративную почту + дополнительные символы(если необходимо) example - danwilliams@mahoney.com
    """
    if is_added_symbols:
        return fake.company_email() + ''.join(generate_symbol)
    else:
        return fake.company_email()