from typing import List
from app.repository.i_repository import IRepository, Singleton
from app.domain.client import Client


class ClientRepository(IRepository, Singleton):
    def __init__(self) -> None:
        self.db = {}

    def save(self, client: Client) -> None:
        self.db[client.id] = client.to_dict()

    def get(self, id: str) -> Client:
        client = self.db.get(id)
        if client:
            return Client.from_dict(client)
        raise

    def get_all(self) -> List[Client]:
        values = self.db.values()
        clients = []
        for client in values:
            clients.append(Client.from_dict(client))

        return clients
