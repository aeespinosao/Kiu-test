from app.repository.ship_repository import ShipRepository
from app.domain.ship import Ship
from app.domain.city import City


class CreateShipUseCase:
    def __init__(self, ship_repository: ShipRepository) -> None:
        self.ship_repository = ship_repository

    def execute(self, origin: City, destination: City, client_id) -> Ship:
        ship = Ship(origin, destination, client_id)
        self.ship_repository.save(ship)
        return ship
