from datetime import date
from faker import Faker
import random
from typing import Any


def generate_phone_number(fake: Faker = Faker("ru-RU"),
                          is_added_symbols: bool = False,
                          generate_symbols: Any = None) -> date | Any:
    """

    :param generate_symbol: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует тел номер + дополнительные символы(если необходимо) example - 8 (183) 689-5542
    """
    if is_added_symbols:
        return fake.phone_number() + ''.join(generate_symbols)
    else:
        return fake.phone_number()