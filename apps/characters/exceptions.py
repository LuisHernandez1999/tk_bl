class CharacterNotFoundException(Exception):
    def __init__(self, message="Character not found"):
        self.message = message
        super().__init__(self.message)

class CharacterInvalidDataException(Exception):
    def __init__(self, message="Invalid character data"):
        self.message = message
        super().__init__(self.message)
