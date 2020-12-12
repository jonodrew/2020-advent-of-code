from helpers.helpers import ReadLines
import operator
from typing import Tuple, Callable, Dict


class NavSystem(ReadLines):
    def __init__(self, file_input=None):
        super(NavSystem, self).__init__(file_input, "twelve")
        self._cardinal_directions = ["N", "E", "S", "W"]
        self._current_facing: str = "E"
        self._current_north: int = 0
        self._current_east: int = 0

    def _rotate(self, instruction: str) -> None:
        directions = {"R": operator.add, "L": operator.sub}
        direction = instruction[0]
        operation = directions[direction]
        value = int(instruction[1:]) / 90
        current_index = self._cardinal_directions.index(self._current_facing)
        new_index = int(
            (operation(current_index, value) + len(self._cardinal_directions)) % 4
        )
        self._current_facing = self._cardinal_directions[new_index]
        return None

    def _move_in_cardinal_direction(self, instruction: str) -> None:
        if instruction[0] == "F":
            instruction = instruction.replace("F", self._current_facing)
        movements: Dict[str, Tuple[Callable, str]] = {
            "N": (operator.add, "_current_north"),
            "E": (operator.add, "_current_east"),
            "S": (operator.sub, "_current_north"),
            "W": (operator.sub, "_current_east"),
        }
        direction = instruction[0]
        value = int(instruction[1:])
        operation, cardinality = movements[direction]
        self.__setattr__(
            cardinality, operation(self.__getattribute__(cardinality), value)
        )
        return None

    def execute(self):
        for instruction in self.inputs:
            direction = instruction[0]
            if direction in {"L", "R"}:
                self._rotate(instruction)
            elif direction in self._cardinal_directions or direction == "F":
                self._move_in_cardinal_direction(instruction)
            else:
                raise ValueError
        return None

    def manhattan_distance(self):
        return sum((abs(self._current_north), abs(self._current_east)))


class Ship(NavSystem):
    def __init__(self, file_input=None):
        super(Ship, self).__init__(file_input)


class WayPoint(NavSystem):
    def __init__(self, file_input=None):
        super(WayPoint, self).__init__(file_input)


class DayTwelve(ReadLines):
    def __init__(self, file_input=None):
        super(DayTwelve, self).__init__(file_input, "twelve")
