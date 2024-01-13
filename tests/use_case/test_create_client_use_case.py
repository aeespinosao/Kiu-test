import unittest
from unittest.mock import MagicMock
from app.use_case.create_client_use_case import CreateClientUseCase
from app.repository.client_repository import ClientRepository
from app.domain.client import Client


class TestCreateClientUseCase(unittest.TestCase):
    def test_execute(self):
        # Arrange
        mock_client_repository = MagicMock(spec=ClientRepository)
        create_client_use_case = CreateClientUseCase(mock_client_repository)

        # Act
        client_id = "123"
        client_name = "John Doe"
        created_client = create_client_use_case.execute(client_id, client_name)

        # Assert
        # Check that the save method on the client repository
        # was called with the correct arguments
        mock_client_repository.save.assert_called_once_with(
            Client(id=client_id, name=client_name)
        )

        # Check that the returned client matches the expected client
        self.assertEqual(created_client.id, client_id)
        self.assertEqual(created_client.name, client_name)
