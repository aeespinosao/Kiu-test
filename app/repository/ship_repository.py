from typing import List
from app.repository.i_repository import IRepository, Singleton
from app.domain.ship import Ship

class ShipRepository(IRepository, Singleton):
    
    def __init__(self) -> None:
        self.db = {}
        
    def save(self, ship: Ship) -> None:
        self.db[ship.id] = ship.to_dict()
        
    def get(self, id: str) -> Ship:
        ship = self.db.get(id)
        if ship:
            return Ship.from_dict(ship)
        raise 
    
    def get_all(self) -> List[Ship]:
        
        values = self.db.values()
        ships = []
        for ship in values:
            ships.append(Ship.from_dict(ship))
            
        return ships
    
    def get_by_date(self, date: str) -> List[Ship]:
        values = self.db.values()
        ships = []
        for value in values:
            ship = Ship.from_dict(value)
            if ship.date == date:
                ships.append(ship)
            
        return ships
        