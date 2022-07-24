from typing import Union

from rentomatic.requests.error import RequestError


class RoomListValidRequest:
    def __init__(self, filters=None):
        self.filters = filters

    def __bool__(self):
        return True


class RoomListInvalidRequest:
    """
    This class is used when an incoming api request is invalid (due to filters).
    The errors attribute contains all validation errors.
    """

    def __init__(self, errors=None):
        self.errors: list[RequestError] = errors or list()

    def has_errors(self) -> bool:
        return len(self.errors) > 0

    def __bool__(self):
        return False


ACCEPTED_FILTERS = ["code__eq", "price__eq", "price__lt", "price__gt"]


def build_room_list_request(
    filters: dict[str, float] = None,
) -> Union[RoomListValidRequest, RoomListInvalidRequest]:
    """
    If a mapping of valid filters is passed, a RoomListValidRequest object is constructed with those filters and returned.
    If at least one filter is invalid, a RoomListInvalidRequest object is returned. It contains all validation errors.
    A filter is invalid if:
    - the key is not in the list of accepted filters

    :param filters: dictionary mapping filter keys to the corresponding value
    :return: Request object constructed from the filter as specified above
    """
    # todo: refactor to dedicated filters class
    if filters is None:
        return RoomListValidRequest(filters)

    errors = []
    for filter, value in filters.items():
        if filter not in ACCEPTED_FILTERS:
            errors.append(
                RequestError(
                    parameter="filters",
                    message=f"Key {filter} cannot be used. Accepted key are: {ACCEPTED_FILTERS}",
                )
            )

    if errors:
        return RoomListInvalidRequest(errors)

    return RoomListValidRequest(filters)
