import json
import uuid

import pytest

from rentomatic.domain.room import Room
from rentomatic.serializers.room import RoomJsonEncoder


@pytest.fixture
def code():
    return uuid.uuid4()


@pytest.fixture
def init_dict(code):
    return {
        "code": code,
        "size": 200,
        "price": 10,
        "longitude": -0.09998975,
        "latitude": 51.75436293,
    }


def test_serialize_domain_room(init_dict, code):
    room = Room.from_dict(init_dict)
    expected_json = f"""
            {{
                "code": "{code}",
                "size": 200,
                "price": 10,
                "longitude": -0.09998975,
                "latitude": 51.75436293
            }}
        """

    json_room = json.dumps(room, cls=RoomJsonEncoder)

    # transform strings to dict to make comparison easier (order of fields would matter with string)
    assert json.loads(json_room) == json.loads(expected_json)
