class ResponseSuccess:
    def __int__(self, value):
        self.value = value

    def __bool__(self):
        return True
