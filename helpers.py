from typing import List, Union
import itertools


class ReadLines(object):
    def __init__(self, file_input: str):
        with open(file_input) as reader:
            self.inputs: List[str] = [line.rstrip() for line in reader]


class AdventOfCodeHelpers(ReadLines):
    def __init__(self, file_input: Union[str, None] = None, day: str = ""):
        if file_input is None:
            file_input = f"/home/jonathan/projects/2020-advent-of-code/{day}/input.txt"
        super(AdventOfCodeHelpers, self).__init__(file_input)

    def _group(self) -> List[List[str]]:
        return [
            list(group)
            for k, group in itertools.groupby(self.inputs, lambda x: x == "")
            if not k
        ]
