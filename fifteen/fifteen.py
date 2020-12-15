from typing import List, Dict, Tuple


class Recitation:
    def __init__(self, puzzle_input=[14, 3, 1, 0, 9, 5], count_to: int = 2020):
        self.count_to = count_to
        self.inputs = puzzle_input
        self.current_counter = len(puzzle_input)
        self.record: Dict[int, List[int]] = {
            value: [index] for index, value in enumerate(puzzle_input)
        }

    def execute(self) -> int:
        last_value = self.inputs[-1]
        while self.current_counter != self.count_to:
            last_value = self.evaluate(last_value)
            self.current_counter += 1
        return last_value

    def evaluate(self, last_value: int) -> int:
        if last_value not in self.record.keys():
            self.record[last_value] = [self.current_counter - 1]
            return 0
        else:
            self.record[last_value].append(self.current_counter - 1)
            record: List[int] = self.record[last_value]
            return record[-1] - record.pop(-2)
