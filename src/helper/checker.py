import requests
from requests import Response


def positive_status_code(response: Response,
                         status_code: list[int] = [200, 201, 202, 204]) -> str:
    """
    Checks if the response is positive or not.
    :param response: Ответ от сервера
    :param status_code: Список статус кодов с положительным ответом
    :return: Успешность вызова метода положительным ответом
    """
    assert response.status_code in status_code, (f"Actual status code = {response.status_code} not in "
                                                 f"list: {status_code}, Reason: {response.reason}")

    return f"Status code {response} in list {status_code}"


def negative_status_code(response: Response,
                         status_code: list[int] = [400, 403, 404, 422, 425]) -> str:
    """
    Checks if the response is negative or not.
    :param response: Ответ от сервера
    :param status_code: Список статус кодов с положительным ответом
    :return:  Успешность вызова метода отрицательным ответом
    """

    assert response.status_code in status_code, (f"Actual status code = {response.status_code} not in "
                                                 f"list: {status_code}")

    return f"Status code {response} in list {status_code}"
