import random
from typing import Any

from src.data.dictionary import alphabet_lat_low, digits


def generate_symbols(lst: list[str],
                     size_word: int) -> str:
    """
    :param lst: Список символов, который нужно обрабоать
    :param size_word: количство символов
    :return: Собирает сгенерированное слово из символов
    """
    word = ''
    for _ in range(size_word):
        word += random.choice(lst)

    return word


def generate_ppk_reo_id() -> str:
    """
    :return: Генерирует символы для заполнения параметра ППК РЭО ID example - jrstcjry-9x4d-9f8c-dqs8-c3lxyrwvbuxd
    """
    part_1 = generate_symbols(size_word=8, lst=alphabet_lat_low + digits)
    part_2 = generate_symbols(size_word=4, lst=alphabet_lat_low + digits)
    part_3 = generate_symbols(size_word=4, lst=alphabet_lat_low + digits)
    part_4 = generate_symbols(size_word=4, lst=alphabet_lat_low + digits)
    part_5 = generate_symbols(size_word=12, lst=alphabet_lat_low + digits)
    ppk_reo_id = str(f"{part_1}-{part_2}-{part_3}-{part_4}-{part_5}")

    return ppk_reo_id


def generate_choice_list_item(lst: list[Any]) -> Any:
    """
    :param lst: Список из элментов, что нужно выбрать
    :return: Генерирует случайный выбор элемента из листа
    """
    return random.choice(lst)
