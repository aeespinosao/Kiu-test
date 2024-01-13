from app.repository.client_repository import ClientRepository
from app.domain.client import Client


class CreateClientUseCase:
    def __init__(self, client_repository: ClientRepository) -> None:
        self.client_repository = client_repository

    def execute(self, id: str, name: str) -> Client:
        client = Client(id, name)
        self.client_repository.save(client)
        return client
