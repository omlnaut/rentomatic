from typing import Protocol

from rentomatic.domain.room import Room


class IRepository(Protocol):
    def list(self, filters: dict[str, float]) -> list[Room]:
        pass
