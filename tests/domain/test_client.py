import unittest
from app.domain.client import (
    Client,
)


class TestClient(unittest.TestCase):
    def test_client_creation(self):
        client = Client(id="123", name="John Doe")
        self.assertEqual(client.id, "123")
        self.assertEqual(client.name, "John Doe")

    def test_to_dict(self):
        client = Client(id="123", name="John Doe")
        client_dict = client.to_dict()
        self.assertEqual(client_dict, {"id": "123", "name": "John Doe"})

    def test_from_dict(self):
        data = {"id": "123", "name": "John Doe"}
        client = Client.from_dict(data)
        self.assertEqual(client.id, "123")
        self.assertEqual(client.name, "John Doe")

    def test_from_dict_missing_values(self):
        data = {"id": "123"}
        client = Client.from_dict(data)
        self.assertEqual(client.id, "123")
        self.assertIsNone(client.name)

    def test_from_dict_extra_values(self):
        data = {"id": "123", "name": "John Doe", "extra": "value"}
        client = Client.from_dict(data)
        self.assertEqual(client.id, "123")
        self.assertEqual(client.name, "John Doe")
        self.assertFalse(hasattr(client, "extra"))
