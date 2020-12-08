from helpers import ReadLines
from typing import Tuple, List


class DayFive(ReadLines):
    def __init__(
        self, file_path="/home/jonathan/projects/2020-advent-of-code/five/input.txt"
    ):
        super().__init__(file_input=file_path)
        self.seat_ids = sorted(
            [DayFive.identify_seat(seat_code)[2] for seat_code in self.inputs]
        )

    @staticmethod
    def _process_code(code: List[str], _range: Tuple[int, int]) -> int:
        """
        I'm leaving this method in, because it's quite neat - but it has been rendered useless by the more practical _binary_count method below
        """
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
            return DayFive._process_code(code, new_range)

    @staticmethod
    def _binary_count(seat_code: str):
        letter_key = {"F": "0", "L": "0", "B": "1", "R": "1"}
        binary_string_code = "".join([letter_key[letter] for letter in seat_code])
        return int(binary_string_code, 2)

    @staticmethod
    def identify_seat(seat_reference: str) -> Tuple[int, int, int]:
        row = DayFive._binary_count(seat_reference[:7])
        column = DayFive._binary_count(seat_reference[-3:])
        seat_id = row * 8 + column
        return row, column, seat_id

    def highest_id(self):
        return max(self.seat_ids)

    def find_missing_id(self) -> int:
        all_ids = set([i for i in range(min(self.seat_ids), max(self.seat_ids) + 1)])
        seat_ids = set(self.seat_ids)
        return all_ids.difference(seat_ids).pop()
