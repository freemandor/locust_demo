from locust import HttpUser, task


class BaseUser(HttpUser):
    abstract = True
    host = "http://localhost:3000"
    _token: str

    def set_token(self, token):
        self._token = token

    def get_token(self) -> str:
        return self._token

    def login(self, user: str, password: str):
        response = self.client.post("/login", json={"user": user, "password": password})
        assert response.status_code == 200
        token = response.json()['token']
        self.set_token(token)

