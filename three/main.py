from useful import ReadLines
from typing import Tuple


class DayThree(ReadLines):
    def __init__(self, file_path="/three/input.txt"):
        super().__init__(file_path)
        self.pattern = (1, 3)

    def move(self, current_position: Tuple[int, int]) -> Tuple[int, int]:
        if current_position[0] == len(self.inputs) - 1:
            raise NoMoveError
        else:
            new_y = current_position[0] + self.pattern[0]
        if current_position[1] + self.pattern[1] > len(self.inputs[0]):
            new_x = current_position[1] + self.pattern[1] - len(self.inputs[0])
        else:
            new_x = current_position[1] + self.pattern[1]
        return (new_y, new_x)


class NoMoveError(Exception):
    """Raised when user is at bottom of map"""

    pass
