from app.repository.ship_repository import ShipRepository
from app.repository.client_repository import ClientRepository
from app.domain.ship import Ship
from app.domain.city import City
from app.shared.exceptions import KeyNotFoundError, JustForClientsError


class CreateShipUseCase:
    def __init__(
        self, ship_repository: ShipRepository, client_repository: ClientRepository
    ) -> None:
        self.ship_repository = ship_repository
        self.client_repository = client_repository

    def execute(self, origin: City, destination: City, client_id) -> Ship:
        try:
            self.client_repository.get(client_id)
        except KeyNotFoundError:
            raise JustForClientsError("Ship are enabled just for client")
        ship = Ship(origin, destination, client_id)
        self.ship_repository.save(ship)
        return ship
