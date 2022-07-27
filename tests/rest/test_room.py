import json
from unittest import mock

import pytest

from rentomatic.domain.room import Room
from rentomatic.responses import ResponseSuccess, ResponseTypes, ResponseFailure
from ..constants import init_dict, code, serialized_dict


@pytest.fixture
def rooms(init_dict):
    return [Room.from_dict(init_dict)]


@mock.patch("application.rest.room.room_list_use_case", autospec=True)
def test_get_without_filters(mock_use_case, client, serialized_dict, rooms):
    mock_use_case.return_value = ResponseSuccess(rooms)

    response = client.get("/rooms")

    assert json.loads(response.data.decode("UTF-8")) == [serialized_dict]
    mock_use_case.assert_called()
    args, kwargs = mock_use_case.call_args
    assert args[1].filters == {}
    assert response.status_code == 200
    assert response.mimetype == "application/json"


@mock.patch("application.rest.room.room_list_use_case", autospec=True)
def test_get_with_filters(mock_use_case, client, serialized_dict, rooms):
    mock_use_case.return_value = ResponseSuccess(rooms)

    response = client.get("/rooms?filter_price__gt=2&filter_price__lt=6")

    assert json.loads(response.data.decode("UTF-8")) == [serialized_dict]

    mock_use_case.assert_called()
    args, kwargs = mock_use_case.call_args
    assert args[1].filters == {"price__gt": "2", "price__lt": "6"}

    assert response.status_code == 200
    assert response.mimetype == "application/json"


@pytest.mark.parametrize(
    "response_type, expected_status_code",
    [
        (ResponseTypes.PARAMETERS_ERROR, 400),
        (ResponseTypes.RESOURCE_ERROR, 404),
        (ResponseTypes.SYSTEM_ERROR, 500),
    ],
)
@mock.patch("application.rest.room.room_list_use_case")
def test_get_response_failures(
    mock_use_case, client, response_type, expected_status_code,
):
    mock_use_case.return_value = ResponseFailure(
        response_type, message="Just an error message",
    )

    http_response = client.get("/rooms?dummy_request_string")

    mock_use_case.assert_called()

    assert http_response.status_code == expected_status_code
