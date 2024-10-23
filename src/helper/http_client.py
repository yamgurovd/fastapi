import os
import requests
from requests import Request, Response
from dotenv import load_dotenv

load_dotenv()


class HttpClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        self.api_client = requests.Session()

    def send_request(self, request: Request) -> Response:
        request = request
        request.url = self.base_url + request.url

        request = self.api_client.prepare_request(request)
        response = self.api_client.send(request)

        return response


user_api_client = HttpClient(base_url=os.getenv("BASE_URL"))
