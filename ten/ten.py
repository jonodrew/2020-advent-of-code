from helpers import AdventOfCodeHelpers
from typing import List
import functools


class DayTen(AdventOfCodeHelpers):
    def __init__(self, file_input=None):
        super(DayTen, self).__init__(file_input=file_input, day="ten")
        self.devices: List[int] = [int(device) for device in self.inputs]
        self.devices.extend([max(self.devices) + 3, 0])
        self.devices.sort()
        self.joltage_differences = {1: 0, 2: 0, 3: 0}
        self._valid_paths = 0
        self.max_joltage = max(self.devices)

    def jolts_multiplied(self, differences_to_multiply: List[int]) -> int:
        values = [self.joltage_differences[key] for key in differences_to_multiply]
        return self.prod(values)

    def execute(self):
        for i, device in enumerate(self.devices):
            try:
                self._joltage_difference(i)
            except IndexError:
                # at end of list
                break

    def _joltage_difference(self, current_index: int) -> None:
        device = self.devices[current_index]
        next_device = self.devices[current_index + 1]
        difference = next_device - device
        self.joltage_differences[difference] += 1

    def total_combinations(self) -> int:
        self._valid_paths += self._test_path()
        return self._valid_paths

    @functools.lru_cache
    def _test_path(self, current_value: int = 0):
        if current_value == max(self.devices):
            #  found a valid path!
            return 1
        else:
            #  at a junction
            paths_on_this_branch = 0
            for i in range(1, 4):
                if current_value + i in self.devices:
                    #  if next step exists
                    paths_on_this_branch += self._test_path(current_value + i)
            return paths_on_this_branch
