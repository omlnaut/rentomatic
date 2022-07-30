from typing import Protocol, Union

from rentomatic.domain.room import Room


class IRepository(Protocol):
    def list(self, filters: dict[str, Union[str, int]]) -> list[Room]:
        pass
