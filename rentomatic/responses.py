from typing import Union, Any

from rentomatic.requests.room_list import RoomListInvalidRequest


class ResponseTypes:
    PARAMETERS_ERROR = "ParametersError"
    RESOURCE_ERROR = "ResourceError"
    SYSTEM_ERROR = "SystemError"
    SUCCESS = "Success"


class ResponseSuccess:
    def __init__(self, value: Any):
        self.value = value
        self.response_type = ResponseTypes.SUCCESS

    def __bool__(self):
        return True


class ResponseFailure:
    def __init__(self, response_type: str, message: Union[str, Exception]):
        self.response_type = response_type
        self.message = self._format_msg(message)

    def __bool__(self):
        return False

    @property
    def value(self) -> dict[str, str]:
        return {"type": self.response_type, "message": self.message}

    def _format_msg(self, message: Union[str, Exception]) -> str:
        if isinstance(message, Exception):
            return f"Exception: {message}"

        return message


def build_response_from_invalid_request(
    request: RoomListInvalidRequest,
) -> ResponseFailure:
    msg = _build_error_msg(request)
    return ResponseFailure(ResponseTypes.PARAMETERS_ERROR, msg)


def _build_error_msg(request: RoomListInvalidRequest) -> str:
    msg = "\n".join(f"{error.parameter}: {error.message}" for error in request.errors)
    return msg
