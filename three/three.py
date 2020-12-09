from helpers import ReadLines
from typing import Tuple
from errors import NoMoveError


class DayThree(ReadLines):
    def __init__(self, file_path="three/input.txt", pattern=(1, 3)):
        super().__init__(file_path)
        self.pattern = pattern
        self.starting_position = (0, 0)
        self.trees_encountered = 0

    def move(self, current_position: Tuple[int, int]) -> Tuple[int, int]:
        if current_position[0] == len(self.inputs) - 1:
            raise NoMoveError
        return (
            current_position[0] + self.pattern[0],
            (current_position[1] + self.pattern[1]) % len(self.inputs[0]),
        )

    def is_tree(self, position: Tuple[int, int]) -> bool:
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
