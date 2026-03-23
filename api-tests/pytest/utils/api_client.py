import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def login(self, username, password):
        response = requests.post(
            f"{self.base_url}/auth/login",
            json={"username": username, "password": password}
        )
        self.token = response.json().get("token")
        return response

    def get_headers(self):
        return {"Authorization": f"Bearer {self.token}"}

    def get(self, endpoint):
        return requests.get(f"{self.base_url}{endpoint}", headers=self.get_headers())

    def post(self, endpoint, payload):
        return requests.post(
            f"{self.base_url}{endpoint}",
            json=payload,
            headers=self.get_headers()
        )