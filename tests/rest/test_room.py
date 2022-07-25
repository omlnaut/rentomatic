import json
from unittest import mock

import pytest

from rentomatic.domain.room import Room
from rentomatic.responses import ResponseSuccess
from ..constants import init_dict, code, serialized_dict


@pytest.fixture
def rooms(init_dict):
    return [Room.from_dict(init_dict)]


@mock.patch("application.rest.room.room_list_use_case", autospec=True)
def test_get(mock_use_case, client, serialized_dict, rooms):
    mock_use_case.return_value = ResponseSuccess(rooms)

    response = client.get("/rooms")

    assert json.loads(response.data.decode("UTF-8")) == [serialized_dict]
    mock_use_case.assert_called()
    args, kwargs = mock_use_case.call_args
    assert args[1].filters == {}
    assert response.status_code == 200
    assert response.mimetype == "application/json"
