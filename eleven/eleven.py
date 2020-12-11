from helpers import ReadLines
from typing import List, Tuple
import itertools
import functools


class GameOfChairs(ReadLines):
    def __init__(self, input_path=None):
        super(GameOfChairs, self).__init__(file_input=input_path, day="eleven")
        self._stable_occupation: int = 0
        self._previous_allocation: set = set()
        self._current_configuration: List[List[str]] = [
            list(row) for row in self.inputs
        ]
        self._row_length = len(self._current_configuration[0])
        self._height = len(self._current_configuration)

    def _iterate(self) -> None:
        new_configuration = [
            [
                self._new_status((column_index, row_index))
                for column_index in range(self._row_length)
            ]
            for row_index in range(self._height)
        ]
        self._current_configuration = new_configuration
        self._cell_status.cache_clear()

    def _new_status(self, column_row: Tuple[int, int]) -> str:
        current_cell = self._cell_status(column_row)
        if current_cell == ".":
            return current_cell
        else:
            surrounding_cells = self._check_nearby_cells(column_row)
            return self._apply_rules(current_cell, surrounding_cells.count("#"))

    def _check_nearby_cells(self, column_row: Tuple[int, int]):
        surrounding_cells = []
        for co_ords in self._produce_nearby_cells_co_ords(column_row):
            if co_ords == column_row:
                surrounding_cells.append("")
            elif self._out_of_bounds(co_ords):
                surrounding_cells.append("")
            else:
                surrounding_cells.append(self._cell_status(co_ords))
        return surrounding_cells

    def _produce_nearby_cells_co_ords(
        self, column_row: Tuple[int, int]
    ) -> List[Tuple[int, int]]:
        return [
            (column_row[0] + column_offset, column_row[1] + row_offset)
            for row_offset, column_offset in itertools.product(
                range(-1, 2), range(-1, 2)
            )
        ]

    @staticmethod
    def _apply_rules(cell_value: str, surrounding_cell_count: int) -> str:
        if surrounding_cell_count == 0 and cell_value == "L":
            return "#"
        elif surrounding_cell_count >= 4 and cell_value == "#":
            return "L"
        else:
            return cell_value

    @functools.lru_cache
    def _cell_status(self, column_row: Tuple[int, int]) -> str:
        return self._current_configuration[column_row[1]][column_row[0]]

    def _out_of_bounds(self, column_row: Tuple[int, int]) -> bool:
        out_of_bounds = [
            lambda x: x[0] < 0 or x[1] < 0,
            lambda x: x[0] == self._row_length or x[1] == self._height,
        ]
        for rule in out_of_bounds:
            if rule(column_row):
                return True
        else:
            return False

    def execute(self) -> int:
        current_allocation = self._stable_occupation
        while current_allocation not in self._previous_allocation:
            self._previous_allocation.add(current_allocation)
            self._iterate()
            current_allocation = sum(
                [row.count("#") for row in self._current_configuration]
            )
        self._stable_occupation = current_allocation
        return current_allocation


class PartTwo(GameOfChairs):
    def __init__(self, input_path=None):
        super(PartTwo, self).__init__(input_path)

    @staticmethod
    def _apply_rules(cell_value: str, surrounding_cell_count: int) -> str:
        if surrounding_cell_count == 0 and cell_value == "L":
            return "#"
        elif surrounding_cell_count >= 5 and cell_value == "#":
            return "L"
        else:
            return cell_value

    def _produce_nearby_cells_co_ords(
        self, column_row: Tuple[int, int]
    ) -> List[Tuple[int, int]]:
        """
        Everything in sight, where 'in sight' is an uninterrupted straight line in any direction
        """
        directions = {
            "NW": (-1, -1),
            "N": (-1, 0),
            "NE": (-1, 1),
            "E": (0, 1),
            "SE": (1, 1),
            "S": (1, 0),
            "SW": (1, -1),
            "W": (0, -1),
        }
        nearby_cells = []
        for direction, offset in directions.items():
            proposed_tuple: Tuple[int, int] = self._add_tuples(column_row, offset)
            while not self._blocked(proposed_tuple):
                proposed_tuple = self._add_tuples(proposed_tuple, offset)
            if self._out_of_bounds(column_row):
                break
            else:
                nearby_cells.append(proposed_tuple)
        return nearby_cells

    @staticmethod
    def _add_tuples(
        tuple_one: Tuple[int, int], tuple_two: Tuple[int, int]
    ) -> Tuple[int, int]:
        return tuple_one[0] + tuple_two[0], tuple_one[1] + tuple_two[1]

    def _blocked(self, column_row: Tuple[int, int]) -> bool:
        return self._out_of_bounds(column_row) or self._cell_status(column_row) in {
            "#",
            "L",
        }
