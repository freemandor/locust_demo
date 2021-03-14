import random

from locust import between, task

from src.BaseUser import BaseUser


class FastUser(BaseUser):
    wait_time = between(5, 15)

    def on_start(self):
        self.login("fast", "user")

    @task()
    def get_fast_user(self):
        user = str(random.randint(0,4))
        self.client.get(f"/fast_user/{user}", headers={"token": self.get_token()}, name="Fast Users")