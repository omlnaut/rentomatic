import uuid

from ..constants import init_dict, code

from rentomatic.domain.room import Room


def test_room_model_init(code):
    room = Room(code, size=200, price=10, longitude=-0.09998975, latitude=51.75436293)

    assert room.code == code
    assert room.size == 200
    assert room.price == 10
    assert room.longitude == -0.09998975
    assert room.latitude == 51.75436293


def test_room_model_from_dict(init_dict, code):
    room = Room.from_dict(init_dict)

    assert room.code == code
    assert room.size == 200
    assert room.price == 10
    assert room.longitude == -0.09998975
    assert room.latitude == 51.75436293


def test_room_model_to_dict(init_dict):
    room = Room.from_dict(init_dict)

    assert room.to_dict() == init_dict


def test_room_model_comparison(init_dict):
    room1 = Room.from_dict(init_dict)
    room2 = Room.from_dict(init_dict)

    assert room1 == room2
