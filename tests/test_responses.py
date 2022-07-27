import pytest

from rentomatic.requests.error import RequestError
from rentomatic.requests.room_list import RoomListInvalidRequest
from rentomatic.responses import (
    ResponseSuccess,
    ResponseFailure,
    ResponseTypes,
    build_response_from_invalid_request,
)


@pytest.fixture
def generic_response_type():
    return "Response"


@pytest.fixture
def generic_response_message():
    return "Message"


@pytest.fixture
def generic_success_value():
    return "Request succeeded"


def test_response_success_is_true():
    assert bool(ResponseSuccess("")) is True


def test_response_failure_is_false(generic_response_type, generic_response_message):
    response = ResponseFailure(generic_response_type, generic_response_message)

    assert bool(response) is False


def test_response_has_type_and_value(generic_success_value):
    response = ResponseSuccess(generic_success_value)

    assert response.response_type == ResponseTypes.SUCCESS
    assert response.value == generic_success_value


def test_response_failure_has_type_and_message(
    generic_response_type, generic_response_message
):
    response = ResponseFailure(generic_response_type, generic_response_message)

    assert response.response_type == generic_response_type
    assert response.message == generic_response_message
    assert response.value == {
        "type": generic_response_type,
        "message": generic_response_message,
    }


def test_response_failure_initialisation_with_exception(generic_response_type):
    message = "Just an error message"
    response = ResponseFailure(generic_response_type, Exception(message))

    assert bool(response) is False
    assert response.response_type == generic_response_type
    assert response.message == f"Exception: {message}"


def test_response_failure_from_empty_invalid_request():
    response = build_response_from_invalid_request(RoomListInvalidRequest())

    assert bool(response) is False
    assert response.response_type == ResponseTypes.PARAMETERS_ERROR


def test_response_failure_from_invalid_request_with_errors():
    mandatory = "Is mandatory"
    blank = "can't be blank"
    errors = [
        RequestError(parameter="path", message=mandatory),
        RequestError(parameter="path", message=blank),
    ]
    request = RoomListInvalidRequest(errors)

    response = build_response_from_invalid_request(request)

    assert bool(response) is False
    assert response.response_type == ResponseTypes.PARAMETERS_ERROR
    assert response.message == f"path: {mandatory}\npath: {blank}"
