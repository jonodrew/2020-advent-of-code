from helpers import ReadLines
from typing import Tuple


class NoMoveError(Exception):
    """Raised when user is at bottom of map"""

    pass


class DayThree(ReadLines):
    def __init__(self, file_path="/three/input.txt"):
        super().__init__(file_path)
        self.pattern = (1, 3)
        self.starting_position = (0, 0)
        self.trees_encountered = 0

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

    def is_tree(self, position: Tuple[int, int]) -> bool:
        print("TREE")
        return self.inputs[position[0]][position[1]] == "#"

    def proceed(self):
        current_position = self.starting_position
        while current_position[0] < len(self.inputs):
            if self.is_tree(current_position):
                self.trees_encountered += 1
            try:
                current_position = self.move(current_position)
            except NoMoveError:
                break
