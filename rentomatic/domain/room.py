import dataclasses
import uuid
from dataclasses import dataclass
from typing import Any


@dataclass
class Room:
    code: uuid.UUID
    size: int
    price: int
    longitude: float
    latitude: float

    @classmethod
    def from_dict(cls, init_dict: dict[str, Any]) -> "Room":
        return cls(**init_dict)

    def to_dict(self) -> dict[str, Any]:
        return dataclasses.asdict(self)
