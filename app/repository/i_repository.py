from typing import List, TypeVar, Protocol

T = TypeVar("T")


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Additional initialization can be done here
        return cls._instance


class IRepository(Protocol):
    def save(self, element: T) -> None:
        pass

    def get(self, id: str) -> T:
        pass

    def get_all(self) -> List[T]:
        pass
