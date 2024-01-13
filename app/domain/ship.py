from app.domain.city import City
from app.domain.client import Client
from uuid import uuid4
from typing import Dict, Any
from datetime import datetime

class Ship:
    def __init__(self, origin: City, destination: City, client_id: str, price: int = 10, id: str = str(uuid4()), datetime: datetime = datetime.now()) -> None:
        self.origin = origin
        self.destination = destination
        self.client_id = client_id
        self.price = price
        self.id = id
        self.date = datetime.date().isoformat()
        self.time = datetime.time().isoformat()
            
    def to_dict(self):
        return self.__dict__
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Ship':
        return cls(
            origin=data.get('origin'),
            destination=data.get('destination'),
            client_id=data.get('client_id'),
            price=data.get('price'),
            id=data.get('id'),
            datetime=datetime.fromisoformat(f"{data.get('date')} {data.get('time')}")
        )
            