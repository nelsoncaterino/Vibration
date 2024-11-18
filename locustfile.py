from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Temps d'attente entre les requêtes

    @task
    def load_homepage(self):
        self.client.get("http://127.0.0.1:8000/")  # Changez cela si vous souhaitez tester une autre page
