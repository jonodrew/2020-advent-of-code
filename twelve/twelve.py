from helpers import ReadLines
import operator
from typing import Tuple, Callable, Dict, List, Union


class GenericNavSystem:
    def __init__(
        self, instructions: List[Union[str, None]] = [], current_facing: str = "E"
    ):
        self._cardinal_directions = ["N", "E", "S", "W"]
        self.current_north: int = 0
        self.current_east: int = 0
        self.current_facing: str = current_facing
        self.instructions = instructions
        self._operations: Dict = {}

    def rotate(self, instruction: str) -> None:
        directions = {"R": operator.add, "L": operator.sub}
        direction = instruction[0]
        operation = directions[direction]
        value = int(instruction[1:]) / 90
        current_index = self._cardinal_directions.index(self.current_facing)
        new_index = int(
            (operation(current_index, value) + len(self._cardinal_directions)) % 4
        )
        self.current_facing = self._cardinal_directions[new_index]
        return None

    def move_in_cardinal_direction(self, instruction: str) -> None:
        movements: Dict[str, Tuple[Callable, str]] = {
            "N": (operator.add, "current_north"),
            "E": (operator.add, "current_east"),
            "S": (operator.sub, "current_north"),
            "W": (operator.sub, "current_east"),
        }
        direction = instruction[0]
        value = int(instruction[1:])
        operation, cardinality = movements[direction]
        self.__setattr__(
            cardinality, operation(self.__getattribute__(cardinality), value)
        )
        return None

    def move_forward(self, instruction: str):
        instruction = instruction.replace("F", self.current_facing)
        self.move_in_cardinal_direction(instruction)
        return None

    def _generate_operations(self):
        self._operations = {
            ("L", "R"): self.rotate,
            ("N", "W", "S", "E"): self.move_in_cardinal_direction,
            "F": self.move_forward,
        }

    def execute_instruction(self, instruction: str):
        direction = instruction[0]
        for key, operation in self._operations.items():
            if direction in key:
                operation(instruction)
                break
        return None


class WayPoint(GenericNavSystem):
    def __init__(self, start_location: Tuple[int, int] = (1, 10)):
        super(WayPoint, self).__init__()
        self.current_north, self.current_east = start_location
        self._rotations = {
            90: lambda x, y: (y, -x),
            180: lambda x, y: (-x, -y),
            270: lambda x, y: (-y, x),
        }

    def rotate(self, instruction: str) -> None:
        direction = instruction[0]
        value = int(instruction[1:])
        if direction == "L":
            value = self._convert_to_clockwise(value)
        self.current_east, self.current_north = self._rotations[value](
            self.current_east, self.current_north
        )
        return None

    @staticmethod
    def _convert_to_clockwise(value) -> int:
        return 360 - value


class Ship(GenericNavSystem, ReadLines):
    def __init__(self, file_input=None):
        GenericNavSystem.__init__(self)
        ReadLines.__init__(self, day="twelve", file_input=file_input)

    def manhattan_distance(self):
        return sum((abs(self.current_north), abs(self.current_east)))

    def execute(self):
        self._generate_operations()
        for instruction in self.inputs:
            self.execute_instruction(instruction)


class ShipWithWayPoint(Ship):
    def __init__(self, file_input=None):
        super(ShipWithWayPoint, self).__init__(file_input=file_input)
        self._waypoint = WayPoint()

    def move_forward(self, instruction: str):
        value = int(instruction[1:])
        self.current_north += self._waypoint.current_north * value
        self.current_east += self._waypoint.current_east * value

    def rotate(self, instruction: str) -> None:
        self._waypoint.rotate(instruction)

    def move_in_cardinal_direction(self, instruction: str) -> None:
        self._waypoint.move_in_cardinal_direction(instruction)
