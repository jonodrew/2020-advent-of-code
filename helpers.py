from typing import List
import itertools


class ReadLines(object):
    def __init__(self, file_input: str):
        with open(file_input) as reader:
            self.inputs: List[str] = [line.rstrip() for line in reader]


class AdventOfCodeHelpers(ReadLines):
    def _group(self) -> List[List[str]]:
        return [
            list(group)
            for k, group in itertools.groupby(self.inputs, lambda x: x == "")
            if not k
        ]
