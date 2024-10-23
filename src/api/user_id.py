from requests import Request, Response
from src.data.consts import GET_METHOD, PATCH_METHOD, DELETE_METHOD, POST_METHOD
from src.helper.http_client import user_api_client
from src.helper.headers import headers


def get(id_: int) -> Response:
    """
    :param id_: id пользователя
    :return: Данные пользователя
    """

    request = Request(
        method=GET_METHOD,
        url=f"/users/{id_}",
        headers=headers,
    )

    return user_api_client.send_request(request)


def post(user_id: int,
         first_name: str,
         last_name: str,
         patronymic: str,
         age: int,
         position: str,
         company: str) -> Response:
    """
        :param user_id: Id пользователя
        :param first_name: Имя пользователя
        :param last_name: Фамилия пользователя
        :param patronymic: Отчество пользователя
        :param age: возраст
        :param position: Должность
        :param company: Название компании
        :return: Создание нового пользователя
        """

    request = Request(
        method=POST_METHOD,
        url=f"users/{user_id}?first_name={first_name}&last_name={last_name}&patronymic={patronymic}&age={age}&position={position}&company={company}",
        headers=headers,
        # data=json.dumps(payload),
    )

    return user_api_client.send_request(request)


def patch(user_id: int,
          first_name: str,
          last_name: str,
          patronymic: str,
          age: int,
          position: str,
          company: str) -> Response:
    """
    :param user_id: id пользователя
    :param first_name: Имя
    :param last_name: Фамилия
    :param patronymic: Отчество
    :param age: Возраст
    :param position: Должность
    :param company: Название организации
    :return: Изменение данных пользователя
    """

    request = Request(
        method=PATCH_METHOD,
        url=f"/users/{user_id}?first_name={first_name}&last_name={last_name}&patronymic={patronymic}&age={age}&position={position}&company={company}",
        headers=headers,
    )

    return user_api_client.send_request(request)


def delete(id_: int) -> Response:
    """
    :param id_: id пользователя
    :return: Удаление записи пользователя
    """

    request = Request(
        method=DELETE_METHOD,
        url=f"users/{id_}",
        headers=headers,
    )

    return user_api_client.send_request(request)
