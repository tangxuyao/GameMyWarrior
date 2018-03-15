import json
from locust import HttpLocust, TaskSet, task

"""https://docs.locust.io"""

class MyTaskSet(TaskSet):
    def on_start(self):
        self.signup()

    @task(1)
    def signup(self):
        r = self.client.post("/signup")
        arg = json.loads(r.content.decode("utf-8"))
        token = arg['token']
        payload = {'token': token, 'name': 'ImLocust'}
        self.client.post("/startgame", payload)
        # print("Response:", r2.status_code)


class WebsiteUser(HttpLocust):
    task_set = MyTaskSet
    host = "http://localhost:8811/v1"
    min_wait = 1000
    max_wait = 5000
