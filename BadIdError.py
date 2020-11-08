class BadIdError(Exception):
    def __init__(self, id, massage="wrong type from id"):
        self.id = id
        self.massage = massage
        super().__init__(self.massage)
