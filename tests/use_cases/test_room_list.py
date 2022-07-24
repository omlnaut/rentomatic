import uuid
from unittest import mock

import pytest

from rentomatic.domain.room import Room
from rentomatic.repository.interface import IRepository
from rentomatic.requests.room_list import RoomListValidRequest, build_room_list_request
from rentomatic.responses import ResponseTypes
from rentomatic.use_cases.room_list import room_list_use_case


@pytest.fixture
def domain_rooms():
    room_1 = Room(
        code=uuid.uuid4(),
        size=215,
        price=39,
        longitude=-0.09998975,
        latitude=51.75436293,
    )

    room_2 = Room(
        code=uuid.uuid4(),
        size=405,
        price=66,
        longitude=0.18228006,
        latitude=51.74640997,
    )

    room_3 = Room(
        code=uuid.uuid4(),
        size=56,
        price=60,
        longitude=0.27891577,
        latitude=51.45994069,
    )

    room_4 = Room(
        code=uuid.uuid4(),
        size=93,
        price=48,
        longitude=0.33894476,
        latitude=51.39916678,
    )

    return [room_1, room_2, room_3, room_4]


@pytest.fixture
def repo(domain_rooms):
    r = mock.create_autospec(IRepository)
    return r


def test_room_list_without_parameters(domain_rooms, repo):
    repo.list.return_value = domain_rooms
    request = RoomListValidRequest()

    response = room_list_use_case(repo, request)

    assert bool(response) is True
    repo.list.assert_called_with(filters=None)
    assert response.value == domain_rooms


def test_room_list_with_filters(domain_rooms, repo):
    repo.list.return_value = domain_rooms
    qry_filters = {"code__eq": 5}
    request = build_room_list_request(filters=qry_filters)

    response = room_list_use_case(repo, request)

    assert bool(response) is True
    repo.list.assert_called_with(filters=qry_filters)
    assert response.value == domain_rooms


def test_room_list_handles_generic_repository_error(repo):
    msg = "Just an error message"
    repo.list.side_effect = Exception(msg)

    request = build_room_list_request(filters={})

    response = room_list_use_case(repo, request)

    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.SYSTEM_ERROR,
        "message": f"Exception: {msg}",
    }


def test_room_list_handles_bad_request():
    repo = mock.Mock()
    invalid_filter_name = "invalid_filter"

    request = build_room_list_request(filters={invalid_filter_name: 0})

    response = room_list_use_case(repo, request)

    assert bool(response) is False
    assert response.value["type"] == ResponseTypes.PARAMETERS_ERROR
    assert invalid_filter_name in response.value["message"]
