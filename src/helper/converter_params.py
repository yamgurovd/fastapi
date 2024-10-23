import urllib
from urllib import parse


def convert(url: str,
            params: dict) -> str:
    """
    :param url: Часть URl c которым нужно соеденить параметры
    :param params: Словарь из параметров, которое нужно обработать
    :return: URL + параметры для endpoint
    """
    first = True
    for i in params:
        if params[i] is None:
            continue
        if first is True:
            url += urllib.parse.urlencode({i: params[i]})
            first = False
        else:
            url += "&" + urllib.parse.urlencode({i: params[i]})
    return url
