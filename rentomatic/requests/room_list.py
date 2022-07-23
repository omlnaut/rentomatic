from typing import Union


class RoomListValidRequest:
    def __init__(self, filters=None):
        self.filters = filters

    def __bool__(self):
        return True


class RoomListInvalidRequest:
    def __init__(self, errors: list):
        self.errors = errors

    def has_errors(self) -> bool:
        return len(self.errors) > 0


def build_room_list_request(
    filters=None,
) -> Union[RoomListValidRequest, RoomListInvalidRequest]:
    """

    :param filters:
    :return:
    """
    return RoomListValidRequest(filters)
