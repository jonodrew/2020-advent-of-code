from helpers import ReadLines
from typing import Tuple, List


class DayFive(ReadLines):
    def __init__(
        self, file_path="/home/jonathan/projects/2020-advent-of-code/five/input.txt"
    ):
        super().__init__(file_input=file_path)

    def _process_code(self, code: List[str], _range: Tuple[int, int]) -> int:
        if len(code) == 1:
            keys = {"L": 0, "F": 0, "R": 1, "B": 1}
            return _range[keys[code[0]]]
        else:
            next_letter = code.pop(0)
            mid_point = int((_range[1] + 1 - _range[0]) / 2)
            if next_letter == "F" or next_letter == "L":
                new_range = _range[0], _range[0] + mid_point - 1
            elif next_letter == "B" or next_letter == "R":
                new_range = _range[0] + mid_point, _range[1]
            return self._process_code(code, new_range)

    def identify_seat(self, seat_reference: str) -> Tuple[int, int, int]:
        row = self._process_code(list(seat_reference[:7]), (0, 127))
        column = self._process_code(list(seat_reference[-3:]), (0, 7))
        seat_id = row * 8 + column
        return row, column, seat_id
