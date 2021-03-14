from locust import between, task

from src.BaseUser import BaseUser


class FastUser(BaseUser):
    wait_time = between(10, 30)
    

    @task()
    def login(self):
        self.client.get("/fast_user/1")

