class EntityIdException(Exception):
    """Exception jika entity tidak ada ID."""

    def __init__(self, message):
        self.message = message


class EntityNotFoundException(Exception):
    """Exception jika entity yang dicari tidak ada. """

    def __init__(self, message):
        self.message = message
