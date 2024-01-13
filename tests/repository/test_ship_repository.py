import unittest
from datetime import timedelta, datetime as dt

from app.repository.ship_repository import ShipRepository
from app.domain.ship import Ship
from app.shared.exceptions import KeyNotFoundError
from app.domain.city import City


class TestShipRepository(unittest.TestCase):
    def setUp(self):
        self.ship_repository = ShipRepository()

    def test_save_and_get(self):
        ship_id = "123"
        origin_city = City.MEDELLIN
        destination_city = City.CARTAGENA
        client_id = "456"
        datetime = dt.now()

        ship = Ship(
            id=ship_id,
            origin=origin_city,
            destination=destination_city,
            client_id=client_id,
            datetime=datetime,
        )

        # Save the ship to the repository
        self.ship_repository.save(ship)

        # Retrieve the ship from the repository
        retrieved_ship = self.ship_repository.db.get(ship_id)

        # Assert that the retrieved ship matches the original ship
        self.assertDictEqual(retrieved_ship, ship.to_dict())

    def test_get_nonexistent_ship(self):
        # Attempt to retrieve a ship with a nonexistent ID
        with self.assertRaises(KeyNotFoundError) as context:
            self.ship_repository.get("nonexistent_id")

        # Optionally, you can check the exception message
        self.assertEqual(
            str(context.exception), "Ship with ID 'nonexistent_id' not found."
        )

    def test_get_all(self):
        # Save two ships to the repository
        ship1 = Ship(
            id="1",
            origin=City.MEDELLIN,
            destination=City.CARTAGENA,
            client_id="123",
            datetime=dt.now(),
        )
        ship2 = Ship(
            id="2",
            origin=City.CARTAGENA,
            destination=City.SANTA_MARTA,
            client_id="456",
            datetime=dt.now(),
        )
        self.ship_repository.save(ship1)
        self.ship_repository.save(ship2)

        # Retrieve all ships from the repository
        all_ships = self.ship_repository.get_all()

        # Assert that the retrieved ships match the saved ships
        self.assertListEqual([ship1, ship2], all_ships)

    def test_get_all_empty_repository(self):
        # Retrieve all ships from an empty repository
        all_ships = self.ship_repository.get_all()

        # Assert that the result is an empty list
        self.assertEqual(all_ships, [])

    def test_get_by_date(self):
        # Save three ships to the repository
        ship1 = Ship(
            id="1",
            origin=City.MEDELLIN,
            destination=City.CARTAGENA,
            client_id="123",
            datetime=dt.now(),
        )
        ship2 = Ship(
            id="2",
            origin=City.CARTAGENA,
            destination=City.SANTA_MARTA,
            client_id="456",
            datetime=dt.now() - timedelta(days=1),
        )
        ship3 = Ship(
            id="3",
            origin=City.SANTA_MARTA,
            destination=City.BOGOTA,
            client_id="789",
            datetime=dt.now(),
        )
        self.ship_repository.save(ship1)
        self.ship_repository.save(ship2)
        self.ship_repository.save(ship3)

        # Retrieve ships for a specific date
        ships_for_date = self.ship_repository.get_by_date(dt.now().date().isoformat())

        # Assert that the retrieved ships match the expected ones
        self.assertEqual(len(ships_for_date), 2)
        self.assertIn(ship1, ships_for_date)
        self.assertIn(ship3, ships_for_date)
