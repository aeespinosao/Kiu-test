import unittest
from app.repository.client_repository import ClientRepository
from app.domain.client import Client
from app.shared.exceptions import KeyNotFoundError


class TestClientRepository(unittest.TestCase):
    def setUp(self):
        # Create a new ClientRepository instance for each test
        self.client_repository = ClientRepository()

    def test_save_success(self):
        client_id = "123"
        client_name = "John Doe"
        client = Client(id=client_id, name=client_name)

        # Save the client to the repository
        self.client_repository.save(client)

        # Retrieve the client from the repository
        client_in_db = self.client_repository.db.get(client_id)

        # Assert that the retrieved client matches the original client
        self.assertDictEqual(client_in_db, client.to_dict())

    def test_get_nonexistent_client(self):
        # Attempt to retrieve a client with a nonexistent ID
        with self.assertRaises(KeyNotFoundError) as context:
            self.client_repository.get("nonexistent_id")

        self.assertEqual(
            str(context.exception), "Client with ID 'nonexistent_id' not found."
        )

    def test_get_all(self):
        # Save two clients to the repository
        client1 = Client(id="1", name="Alice")
        client2 = Client(id="2", name="Bob")
        self.client_repository.save(client1)
        self.client_repository.save(client2)

        # Retrieve all clients from the repository
        all_clients = self.client_repository.get_all()

        # Assert that the retrieved clients match the saved clients
        self.assertListEqual([client1, client2], all_clients)

    def test_get_all_empty_repository(self):
        # Retrieve all clients from an empty repository
        all_clients = self.client_repository.get_all()

        # Assert that the result is an empty list
        self.assertEqual(all_clients, [])
