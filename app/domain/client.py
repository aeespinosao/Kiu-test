from typing import Any, Dict


class Client:
    def __init__(self, id: str, name: str) -> None:
        self.id = id
        self.name = name

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Client":
        return cls(id=data.get("id"), name=data.get("name"))

    def __eq__(self, other):
        if isinstance(other, Client):
            return self.id == other.id and self.name == other.name
        return False
