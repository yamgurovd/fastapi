from datetime import date
from faker import Faker
from typing import Any


def generate_text(size_text: int,
                  fake: Faker = Faker("ru-RU"),
                  is_added_symbols: bool = False,
                  generate_symbols: Any = None) -> date | Any:
    """

    :param generate_symbols: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return: Генерирует текст + дополнительные символы(если необходимо) example -  привет мир
    """
    if is_added_symbols:
        return fake.text(max_nb_chars=size_text) + ''.join(generate_symbols)
    else:
        return fake.text(max_nb_chars=size_text)
