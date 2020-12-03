from useful import ReadLines
from typing import Tuple


class DayThree(ReadLines):
    def __init__(self, file_path="/three/input.txt"):
        super().__init__(file_path)
        self.pattern = (1, 3)

    def move(self, current_position: Tuple[int, int]) -> Tuple[int, int]:
        return (current_position + self.pattern[0], current_position + self.pattern[1])
