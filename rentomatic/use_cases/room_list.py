from typing import Union

from rentomatic.repository.interface import IRepository
from rentomatic.requests.room_list import RoomListValidRequest, RoomListInvalidRequest
from rentomatic.responses import (
    ResponseSuccess,
    ResponseFailure,
    ResponseTypes,
    build_response_from_invalid_request,
)


def room_list_use_case(
    repo: IRepository, request: Union[RoomListValidRequest, RoomListInvalidRequest]
) -> Union[ResponseSuccess, ResponseFailure]:

    match request:
        case RoomListInvalidRequest():
            return build_response_from_invalid_request(request)
        case RoomListValidRequest():
            try:
                rooms = repo.list(filters=request.filters)
                return ResponseSuccess(rooms)
            except Exception as e:
                return ResponseFailure(ResponseTypes.SYSTEM_ERROR, e)
