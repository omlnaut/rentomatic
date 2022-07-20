from typing import Any

from rentomatic.domain.room import Room


class MemRepo:
    def __init__(self, data: dict[str, Any]):
        self.data = data

    def list(self) -> list[Room]:
        return [Room.from_dict(i) for i in self.data]
