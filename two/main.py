from typing import Tuple, List

class DayTwo(object):
    def __init__(self):
        with open('two/input.txt', 'r') as reader:
            self.inputs: List = [self.process_input_line(line) for line in reader]

        self.valid_passwords: int = self.check_validity()

    def process_input_line(self, reader_object_line: str) -> Tuple[int, int, str, str]:
        parts = reader_object_line.split(' ')
        min_max = parts[0].split('-')
        min_uses = int(min_max[0])
        max_uses = int(min_max[1])
        letter_rule = parts[1][0]
        password = parts[2].rstrip()
        return (min_uses, max_uses, letter_rule, password)

    def check_password_against_rule(self, line_input: Tuple[int, int, str, str]) -> bool:
        occurences = line_input[3].count(line_input[2])
        return occurences >= line_input[0] and occurences <= line_input[1]

    def check_validity(self) -> int:
        return [self.check_password_against_rule(line_input) for line_input in self.inputs].count(True)


class DayTwoPartTwo(DayTwo):
    def __init__(self):
        super().__init__()

    def check_password_against_rule(self, line_input: Tuple[int, int, str, str]) -> bool:
        location_one = line_input[0] - 1
        location_two = line_input[1] - 1
        values_at_locations = (line_input[3][location_one], line_input[3][location_two])
        return values_at_locations.count(line_input[2]) == 1

d = DayTwo()
print(d.valid_passwords)