import unittest
from unittest.mock import MagicMock
from datetime import timedelta, datetime as dt

from app.use_case.generate_report_use_case import GenerateReportUseCase
from app.repository.ship_repository import ShipRepository
from app.domain.ship import Ship
from app.domain.city import City


class TestGenerateReportUseCase(unittest.TestCase):
    def test_execute(self):
        # Arrange
        mock_ship_repository = MagicMock(spec=ShipRepository)
        generate_report_use_case = GenerateReportUseCase(mock_ship_repository)

        date = "2022-01-01"
        ship1 = Ship(
            id="1",
            origin=City.MEDELLIN,
            destination=City.CARTAGENA,
            client_id="123",
            datetime=dt.now(),
            price=20,
        )
        Ship(
            id="2",
            origin=City.CARTAGENA,
            destination=City.SANTA_MARTA,
            client_id="456",
            datetime=dt.now() - timedelta(days=1),
            price=30,
        )
        ship3 = Ship(
            id="2",
            origin=City.CARTAGENA,
            destination=City.SANTA_MARTA,
            client_id="456",
            datetime=dt.now(),
            price=30,
        )
        ships = [ship1, ship3]
        total_price = sum(ship.price for ship in ships)

        mock_ship_repository.get_by_date.return_value = ships

        # Act
        result = generate_report_use_case.execute(date)

        # Assert
        # Check that the get_by_date method on the ship repository
        # was called with the correct date
        mock_ship_repository.get_by_date.assert_called_once_with(date)

        # Check that the returned result matches the expected result
        expected_result = (
            f"The date {date} was shipped {len(ships)} "
            f"packages with a total price of {total_price}"
        )
        self.assertEqual(result, expected_result)
