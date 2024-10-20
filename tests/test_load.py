from locust import HttpUser, task, between

class StripeUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def create_event(self):
        self.client.post("/api/events/", json={
            "kind": "customer.created",
            "stripe_id": "cus_load_test"
        })
