class RoomListRequest:
    @classmethod
    def from_dict(cls, dictionary):
        return cls()

    def __bool__(self):
        return True
