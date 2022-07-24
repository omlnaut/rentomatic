import pytest

from rentomatic.responses import ResponseSuccess, ResponseFailure


@pytest.fixture
def generic_response_type():
    return "Response"


@pytest.fixture
def generic_response_message():
    return "Message"


def test_response_success_is_true():
    assert bool(ResponseSuccess(None)) is True


def test_response_failure_is_false(generic_response_type, generic_response_message):
    response = ResponseFailure(generic_response_type, generic_response_message)

    assert bool(response) is False
