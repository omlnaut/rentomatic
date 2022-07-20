import json

from rentomatic.domain.room import Room


class RoomJsonEncoder(json.JSONEncoder):
    def default(self, room: Room):
        try:
            to_serialize = {
                "code": str(room.code),
                "size": room.size,
                "price": room.price,
                "latitude": room.latitude,
                "longitude": room.longitude,
            }
            return to_serialize
        except AttributeError:
            return super().default(room)
