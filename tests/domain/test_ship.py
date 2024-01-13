import unittest
from app.domain.city import City
from app.domain.ship import (
    Ship,
)
from uuid import uuid4
from datetime import datetime


class TestShip(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.origin_city = City.MEDELLIN
        cls.destination_city = City.CARTAGENA

    def test_ship_creation(self):
        ship = Ship(
            origin=self.origin_city,
            destination=self.destination_city,
            client_id="123",
            price=20,
            id=str(uuid4()),
            datetime=datetime(
                2022, 1, 1, 12, 0
            ),  # Assuming a specific datetime for testing
        )

        self.assertEqual(ship.origin, self.origin_city)
        self.assertEqual(ship.destination, self.destination_city)
        self.assertEqual(ship.client_id, "123")
        self.assertEqual(ship.price, 20)
        self.assertIsInstance(ship.id, str)
        self.assertEqual(ship.date, "2022-01-01")
        self.assertEqual(ship.time, "12:00:00")

    def test_to_dict(self):
        ship = Ship(
            origin=self.origin_city,
            destination=self.destination_city,
            client_id="123",
            price=20,
            id=str(uuid4()),
            datetime=datetime(
                2022, 1, 1, 12, 0
            ),  # Assuming a specific datetime for testing
        )

        ship_dict = ship.to_dict()
        expected_dict = {
            "origin": self.origin_city,
            "destination": self.destination_city,
            "client_id": "123",
            "price": 20,
            "id": ship.id,
            "date": "2022-01-01",
            "time": "12:00:00",
        }
        self.assertEqual(ship_dict, expected_dict)

    def test_from_dict(self):
        data = {
            "origin": self.origin_city,
            "destination": self.destination_city,
            "client_id": "123",
            "price": 20,
            "id": str(uuid4()),
            "date": "2022-01-01",
            "time": "12:00:00",
        }

        ship = Ship.from_dict(data)

        self.assertEqual(ship.origin, self.origin_city)
        self.assertEqual(ship.destination, self.destination_city)
        self.assertEqual(ship.client_id, "123")
        self.assertEqual(ship.price, 20)
        self.assertIsInstance(ship.id, str)
        self.assertEqual(ship.date, "2022-01-01")
        self.assertEqual(ship.time, "12:00:00")
