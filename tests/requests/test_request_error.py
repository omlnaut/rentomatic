from rentomatic.requests.error import RequestError


def test_request_error_initialization():
    message = "message"
    parameter = "parameter"

    error = RequestError(parameter=parameter, message=message)

    assert error.parameter == parameter
    assert error.message == message
