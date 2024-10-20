import json
from django.test import TestCase, Client

class WebhookTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_webhook_processing(self):
        payload = {
            "id": "evt_test123",
            "type": "transfer.created",
            "data": {
                "object": {
                    "amount": 1000,
                    "currency": "usd",
                    "status": "paid",
                    "stripe_id": "tr_test123",
                }
            }
        }

        response = self.client.post("/webhooks/stripe/", data=json.dumps(payload), content_type="application/json")
        assert response.status_code == 200
        assert response.json().get("received") is True  # Убедиться, что вебхук успешно обработан
