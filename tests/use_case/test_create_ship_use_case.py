import unittest
from unittest.mock import MagicMock
from app.use_case.create_ship_use_case import CreateShipUseCase
from app.repository.ship_repository import ShipRepository
from app.repository.client_repository import ClientRepository
from app.domain.ship import Ship
from app.domain.city import City
from app.shared.exceptions import KeyNotFoundError, JustForClientsError


class TestCreateShipUseCase(unittest.TestCase):
    def setUp(self):
        self.mock_ship_repository = MagicMock(spec=ShipRepository)
        self.mock_client_repository = MagicMock(spec=ClientRepository)
        self.create_ship_use_case = CreateShipUseCase(
            ship_repository=self.mock_ship_repository,
            client_repository=self.mock_client_repository,
        )

    def test_execute_with_valid_client(self):
        # Arrange
        origin_city = City.MEDELLIN
        destination_city = City.CARTAGENA
        client_id = "456"
        mocked_client = MagicMock()  # Mock the client returned by the client repository
        self.mock_client_repository.get.return_value = mocked_client

        # Act
        created_ship = self.create_ship_use_case.execute(
            origin_city, destination_city, client_id
        )

        # Assert
        # Check that the client repository's get method was called
        # with the correct client_id
        self.mock_client_repository.get.assert_called_once_with(client_id)

        # Check that the save method on the ship repository
        # was called with the correct arguments
        self.mock_ship_repository.save.assert_called_once_with(
            Ship(origin=origin_city, destination=destination_city, client_id=client_id)
        )

        # Check that the returned ship matches the expected ship
        self.assertEqual(created_ship.origin, origin_city)
        self.assertEqual(created_ship.destination, destination_city)
        self.assertEqual(created_ship.client_id, client_id)

    def test_execute_with_invalid_client(self):
        # Arrange
        origin_city = City.MEDELLIN
        destination_city = City.CARTAGENA
        client_id = "456"
        self.mock_client_repository.get.side_effect = KeyNotFoundError(
            "Client not found"
        )

        # Act/Assert
        with self.assertRaises(JustForClientsError) as context:
            self.create_ship_use_case.execute(origin_city, destination_city, client_id)

        # Check that the exception message matches the expected message
        self.assertEqual(str(context.exception), "Ship are enabled just for client")

        # Check that the client repository's get method
        # was called with the correct client_id
        self.mock_client_repository.get.assert_called_once_with(client_id)

        # Ensure that the save method on the ship repository was not called
        self.mock_ship_repository.save.assert_not_called()
