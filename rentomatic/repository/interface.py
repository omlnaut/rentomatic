from typing import Protocol

from rentomatic.domain.room import Room


class IRepository(Protocol):
    def list(self) -> list[Room]:
        pass
