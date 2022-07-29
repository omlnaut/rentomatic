from typing import Any, Union

from rentomatic.domain.room import Room


class MemRepo:
    def __init__(self, data: list[dict[str, Any]]):
        self.data = data

    def list(self, filters: dict[str, Union[str, int]]) -> list[Room]:
        rooms = [Room.from_dict(i) for i in self.data]

        if "code__eq" in filters:
            rooms = [room for room in rooms if room.code == filters["code__eq"]]

        if "price__eq" in filters:
            rooms = [room for room in rooms if room.price == int(filters["price__eq"])]

        if "price__lt" in filters:
            rooms = [room for room in rooms if room.price < int(filters["price__lt"])]

        if "price__gt" in filters:
            rooms = [room for room in rooms if room.price > int(filters["price__gt"])]

        return rooms
