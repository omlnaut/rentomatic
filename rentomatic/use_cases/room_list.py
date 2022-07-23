from rentomatic.repository.interface import IRepository
from rentomatic.requests.room_list import RoomListRequest
from rentomatic.responses import ResponseSuccess


def room_list_use_case(repo: IRepository, request: RoomListRequest) -> ResponseSuccess:
    rooms = repo.list()

    return ResponseSuccess(rooms)
