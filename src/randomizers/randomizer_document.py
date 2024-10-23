from faker import Faker
import random
from typing import Any


def generate_individual_inn(fake: Faker = Faker("ru-RU"),
                            is_added_symbols: bool = False,
                            generate_symbol: Any = None) -> str:
    """

    :param generate_symbol: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует Физические ИНН + дополнительные символы(если необходимо) example - 499491448195
    """
    if is_added_symbols:
        return fake.individuals_inn() + ''.join(generate_symbol)
    else:
        return fake.individuals_inn()


def generate_business_inn(fake: Faker = Faker("ru-RU"),
                          is_added_symbols: bool = False,
                          generate_symbol: Any = None) -> str:
    """

    :param generate_symbol: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует Физические ИНН + дополнительные символы(если необходимо) example - 499491448195
    """
    if is_added_symbols:
        return fake.businesses_inn() + ''.join(generate_symbol)
    else:
        return fake.businesses_inn()


def generate_kpp(fake: Faker = Faker("ru-RU"),
                 addition_symbols: Any = None) -> str:
    """
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :param addition_symbols: Дополнительные символы, которые необходимо дополнить
    :return: Генерирует КПП + дополнительные символы(если необходимо) example - 8190530479
    """

    if addition_symbols is None:
        return fake.kpp()
    else:
        return fake.kpp() + ''.join(addition_symbols)


def generate_bic(fake: Faker = Faker("ru-RU"),
                 addition_symbols: Any = None) -> str:
    """
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :param addition_symbols: Дополнительные символы, которые необходимо дополнить
    :return: Генерирует БИК + дополнительные символы(если необходимо) example - 2922266579
    """

    if addition_symbols is None:
        return fake.bic()
    else:
        return fake.bic() + ''.join(addition_symbols)


def generate_individual_ogrn(fake: Faker = Faker("ru-RU"),
                             is_added_symbols: bool = False,
                             generate_symbol: Any = None) -> str:
    """

    :param generate_symbol: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует Физические ОГРН + дополнительные символы(если необходимо) example - 307810861953314
    """
    if is_added_symbols:
        return fake.individuals_ogrn() + ''.join(generate_symbol)
    else:
        return fake.individuals_ogrn()


def generate_business_ogrn(fake: Faker = Faker("ru-RU"),
                           is_added_symbols: bool = False,
                           generate_symbol: Any = None) -> str:
    """

    :param generate_symbol: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует Физические ОГРН + дополнительные символы(если необходимо) example - 1048021808174
    """
    if is_added_symbols:
        return fake.businesses_ogrn() + ''.join(generate_symbol)
    else:
        return fake.businesses_ogrn()