
from datetime import date
import random
from typing import Any


def generate_int_digit(period_from: int,
                       period_to: int,
                       is_added_symbols: bool = False,
                       generate_symbols: Any = None) -> date | Any:
    """

    :param period_to: Числовой диапазон от Exaple - 1,
    :param period_from: Числовой диапазон от Exaple - 10
    :param generate_symbolы: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return:  Генерирует целое число+ дополнительные символы(если необходимо) example - 777
    """
    if is_added_symbols:
        return random.randint(period_from, period_to) + ''.join(generate_symbols)
    else:
        return random.randint(period_from, period_to)


def generate_float_digit(period_from: int | float,
                         period_to: int | float,
                         round_after_comma: int,
                         is_added_symbols: bool = False,
                         generate_symbols: Any = None) -> date | Any:
    """

    :param period_to: Числовой диапазон от Exaple - 1, | 1.5
    :param period_from: Числовой диапазон от Exaple - 10, | 10.5
    :param generate_symbol: Дополнительные символы, которые необходимо дополнить
    :param is_added_symbols: Признак генерации дополнительных символов
    :param fake: Экземпляр класса Faker для работы с библиотекой язык default = ru-RU чтоб дполнить ['ru-RU', 'it_IT']
    :return:  Генерирует веещественное число + дополнительные символы(если необходимо) example - 777.22
    """
    if is_added_symbols:
        return round(random.uniform(period_from, period_to), round_after_comma) + ''.join(generate_symbols)
    else:
        return round(random.uniform(period_from, period_to), round_after_comma)
