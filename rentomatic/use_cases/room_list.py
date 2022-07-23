from rentomatic.repository.interface import IRepository
from rentomatic.requests.room_list import RoomListValidRequest
from rentomatic.responses import ResponseSuccess


def room_list_use_case(
    repo: IRepository, request: RoomListValidRequest
) -> ResponseSuccess:
    rooms = repo.list()

    return ResponseSuccess(rooms)
