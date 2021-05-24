import operator
from functools import reduce
from typing import List, Union
import itertools
import os


class ReadLines(object):
    def __init__(self, day: str, file_input: Union[str, None] = None):
        if file_input is None:
            file_input = os.path.join(os.getcwd(), f"{day}/input.txt")
        with open(file_input) as reader:
            self.inputs: List[str] = [line.rstrip() for line in reader]


class AdventOfCodeHelpers(ReadLines):
    def _group(self) -> List[List[str]]:
        return [
            list(group)
            for is_empty_string, group in itertools.groupby(
                self.inputs, lambda x: x == ""
            )
            if not is_empty_string
        ]

    def prod(cls, iterable):
        return reduce(operator.mul, iterable, 1)
