class UnencryptedDataError(Exception):
    def __init__(self, error_value: int):
        self.message = f"This piece of data is unencrypted: {error_value}"
        super(UnencryptedDataError, self).__init__(self.message)


class InfiniteLoopError(Exception):
    """
    Exception raised when an infinite loop is entered.

    Attributes:
        accumulator -- value of accumulator before error
        message -- explanation of the error
    """

    def __init__(self, accumulator):
        self.accumulator = accumulator
        self.message = f"About to enter infinite loop. Accumulator value: {accumulator}"
        super().__init__(self.message)


class NoMoveError(Exception):
    """Raised when user is at bottom of map"""

    pass
