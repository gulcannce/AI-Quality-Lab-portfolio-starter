import requests


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def get(self, path: str):
        return requests.get(
            f"{self.base_url}{path}",
            timeout=10,
        )

    def post(self, path: str, json: dict):
        return requests.post(
            f"{self.base_url}{path}",
            json=json,
            timeout=10,
        )

    def put(self, path: str, json: dict):
        return requests.put(
            f"{self.base_url}{path}",
            json=json,
            timeout=10,
        )

    def delete(self, path: str):
        return requests.delete(
            f"{self.base_url}{path}",
            timeout=10,
        )
