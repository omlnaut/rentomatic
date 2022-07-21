import json
from unittest import mock

import pytest

from rentomatic.domain.room import Room
from ..constants import init_dict, code


@pytest.fixture
def rooms(init_dict):
    return [Room.from_dict(init_dict)]


@mock.patch("application.rest.room.room_list_use_case")
def test_get(mock_use_case, client, init_dict, rooms):
    mock_use_case.return_value = rooms

    response = client.get("/rooms")

    assert json.loads(response.data.decode("UTF-8")) == [
        Room.from_dict(init_dict).to_dict()
    ]
    mock_use_case.assert_called()
    assert response.status_code == 200
    assert response.mimetype == "application/json"
