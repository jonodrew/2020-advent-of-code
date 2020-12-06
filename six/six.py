from helpers import ReadLines
from typing import List, Union
import abc


class DaySix(ReadLines):
    def __init__(self, input_path=None):
        if input_path is None:
            input_path = "/home/jonathan/projects/2020-advent-of-code/six/input.txt"
        super().__init__(input_path)
        self.groups: List[List[str]] = self._group()
        self.sum_of_counts: int = sum(
            self._yeses_in_group(group) for group in self.groups
        )

    def _group(self) -> List[List[str]]:
        groups = []
        group: List[str] = []
        for line in self.inputs:
            if line == "":
                groups.append(group)
                group = []
            else:
                group.append(line)
        return groups

    @staticmethod
    @abc.abstractmethod
    def _yeses_in_group(group: List[str]) -> int:
        return 0


class PartOne(DaySix):
    def __init__(self, input_path=None):
        super(PartOne, self).__init__(input_path)

    @staticmethod
    def _yeses_in_group(group: List[str]) -> int:
        answers = "".join(group)
        return len(set(answers))


class PartTwo(DaySix):
    def __init__(self, input_path=None):
        super(PartTwo, self).__init__(input_path)

    @staticmethod
    def _yeses_in_group(group: List[str]) -> int:
        """
        Return the number of letters that are repeated the same number of time as the original length of the group
        """
        members_in_group = len(group)
        all_answers = "".join(group)
        all_yeses = set(
            [
                letter
                for letter in all_answers
                if all_answers.count(letter) == members_in_group
            ]
        )
        return len(all_yeses)
