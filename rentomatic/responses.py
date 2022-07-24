from dataclasses import dataclass


class ResponseSuccess:
    def __init__(self, value):
        self.value = value

    def __bool__(self):
        return True


class ResponseFailure:
    def __init__(self, type: str, message: str):
        self.type = type
        self.message = message

    def __bool__(self):
        return False
