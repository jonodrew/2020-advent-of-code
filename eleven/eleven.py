from helpers import ReadLines
from typing import List, Tuple
import itertools


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

    def _new_status(self, column_row: Tuple[int, int]) -> str:
        cell_row_index = column_row[1]
        cell_column_index = column_row[0]
        surrounding_cells = []
        current_cell = self._cell_status((cell_column_index, cell_row_index))
        if current_cell == ".":
            return current_cell
        else:
            for column_offset, row_offset in itertools.product(
                range(-1, 2), range(-1, 2)
            ):
                if (row_offset, column_offset) == (0, 0):
                    surrounding_cells.append("")
                else:
                    surrounding_cells.append(
                        self._cell_status(
                            (
                                cell_column_index + column_offset,
                                cell_row_index + row_offset,
                            )
                        )
                    )
            if surrounding_cells.count("#") == 0 and current_cell == "L":
                return "#"
            elif surrounding_cells.count("#") >= 4 and current_cell == "#":
                return "L"
            else:
                return current_cell

    def _cell_status(self, column_row: Tuple[int, int]) -> str:
        out_of_bounds = [
            lambda x: x[0] < 0 or x[1] < 0,
            lambda x: x[0] == self._row_length or x[1] == self._height,
        ]
        for rule in out_of_bounds:
            if rule(column_row):
                return ""
        else:
            return self._current_configuration[column_row[1]][column_row[0]]

    def execute(self) -> int:
        current_allocation = 0
        while current_allocation not in self._previous_allocation:
            self._previous_allocation.add(current_allocation)
            self._iterate()
            current_allocation = sum(
                [row.count("#") for row in self._current_configuration]
            )
        self._stable_occupation = current_allocation
        return current_allocation
