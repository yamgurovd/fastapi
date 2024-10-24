from typing import Any
from requests import Response
from src.helper.checker import negative_status_code, positive_status_code


def _assert_wrapper(value: Any,
                    error_message: str,
                    error_limit: int = 250) -> Any:
    if not value:
        raise AssertionError(error_message[:error_limit])


def status_code(response: Response,
                is_positive: bool = True) -> Any:
    """
    :param response: Проверяемый метод
    :param is_positive: Признак проверки позитивного/негативного набора статус кодов
    :return: Выполняется проверка статус кода в зависимости от контекста провекста проверки
    """

    if is_positive:
        return positive_status_code(response=response)
    else:
        return negative_status_code(response=response)


def status_code_500(response: Response) -> Any:
    """
    :param response: Проверяемый метод
    :return: Выполняет проверку 500 статус кода
    """

    assert response.status_code == 500, f'ER status code: 500 != AR status code: {response.status_code}'


def equal(actual_result: Any,
          expected_result: Any,
          message: str,
          error_message: str | None = None) -> Any:
    """
    :param actual_result: Фактический результат
    :param expected_result: Ожидаемый результат
    :param message: Передоваемый текст
    :param error_message: Текст ошибки
    :return: Проверка
    """
    if error_message is None:
        error_message = (
            f"(equal){message}, actual_result: {actual_result}, expected_result: {expected_result}"
        )
        _assert_wrapper(actual_result == expected_result, error_message=error_message)


def equal_response_json(actual_response_result: Response,
                        expected_response_result: dict,
                        message: str,
                        error_message: str | None = None) -> Any:
    """
    :param actual_response_result: Актуальный JSON ответ
    :param expected_response_result:
    :param message: Передоваемый текст
    :param error_message: Текст ошибки
    :return: Проверка отсутствия записи в словаре
    """

    if error_message is None:
        error_message = (
            f"(equal){message}, actual_result: {actual_response_result}, expected_result: {expected_response_result}"
        )

    key_list = []
    value_list = []
    dictionary = {}

    for key in actual_response_result.json():
        key_list.append(key)

    for key in key_list:
        value_list.append(actual_response_result.json().get(key))

    for i in range(len(key_list)):
        dictionary[key_list[i]] = value_list[i]

    _assert_wrapper(dictionary == expected_response_result, error_message=error_message)


def count_response_param_symbols(expected_size_symbols: int,
                                 response_param_name: str,
                                 response: Response,
                                 message: str,
                                 error_message: str | None = None) -> Any:
    """
    :param expected_size_symbols: Ожидаемое количество символов
    :param response_param_name: название параметра
    :param response: Ответ метода
    :param message: Сообщение, которое необходимо выввести при ошибке
    :param error_message:
    :return: Сравнивает количестов символов
    """
    actual_size_symbols = response.json().get(f'{response_param_name}', f'There is no key {response_param_name}')

    if error_message is None:
        error_message = (
            f"(equal){message}, actual_result: {response_param_name}, expected_result: {expected_size_symbols}"
        )
        _assert_wrapper(expected_size_symbols == len(actual_size_symbols), error_message=error_message)


def is_type_response_param_value(response: Response,
                                 response_param_name: str,
                                 message: str,
                                 is_digit: bool = True,
                                 ) -> Any:
    """
    :param response: Проверяемый метод
    :param response_param_name: названия параметра в JSON формате
    :param message: Сообщение которое будет выводся при неудачной проверка
    :param is_digit: Признак проверки цифр в значении проверки
    :return: Выполняется проверка типа значения параметра в проверяемом методе
    """

    if is_digit:
        assert str(response.json().get(f'{response_param_name}',
                                       f'There is no key {response_param_name}')).isdigit(), f"{message}"
    else:
        assert str(response.json().get(f'{response_param_name}',
                                       f'There is no key {response_param_name}')).isalpha(), f"{message}"
