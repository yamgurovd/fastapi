import json
from requests import Request, Response
from src.data.consts import GET_METHOD
from src.helper.http_client import user_api_client
from src.helper.headers import headers

"""Location: Swagger GET/users"""


def get() -> Response:
    """
    :return: Список пользователей
    """

    request = Request(
        method=GET_METHOD,
        url="users",
        headers=headers,
    )

    return user_api_client.send_request(request)
