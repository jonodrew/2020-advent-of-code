from helpers import ReadLines
from typing import Tuple, List


class Booter(ReadLines):
    def __init__(self, file_input=None, instructions=None):
        self.accumulator = 0
        if instructions is not None:
            self.instructions = instructions
        else:
            super().__init__(file_input, "eight")
            self.instructions: List[Tuple[int, List[str, str]]] = [
                (i, line.split(" ")) for i, line in enumerate(self.inputs)
            ]
        self.instruction_index = 0
        self._instruction_log = []

    def execute_instruction(self, instruction_index: int = 0) -> Tuple[int, int]:
        try:
            next_instruction = self.instructions[instruction_index]
        except IndexError:
            return 0, self.accumulator
        if next_instruction[0] in self._instruction_log:
            raise InfiniteLoopError(self.accumulator)
        else:
            self._instruction_log.append(next_instruction[0])
            if next_instruction[1][0] == "nop":  # no operation
                return self.execute_instruction(instruction_index + 1)
            elif next_instruction[1][0] == "acc":
                self.accumulator += int(next_instruction[1][1])
                return self.execute_instruction(instruction_index + 1)
            elif next_instruction[1][0] == "jmp":
                return self.execute_instruction(
                    instruction_index + int(next_instruction[1][1])
                )
            else:
                raise ValueError("Instruction not valid")


class DayEight(ReadLines):
    def __init__(self, file_input=None):
        super().__init__(file_input, "eight")
        self.instructions: List[Tuple[int, List[str, str]]] = [
            (i, line.split(" ")) for i, line in enumerate(self.inputs)
        ]

    def fix_by_trial_and_error(self) -> Tuple[int, int]:
        """
        One of these instructions is wrong. A 'jmp' should be a 'nop', or vice versa. There's surely a neater way of doing it than this, but this is all
        I've got, so: brute force it is!
        """
        instruction_swap = {"jmp": "nop", "nop": "jmp"}
        for instruction_pair in self.instructions:
            instruction_code = instruction_pair[1][0]
            if instruction_code == "jmp" or instruction_code == "nop":
                new_instructions = self.instructions.copy()
                new_instructions[instruction_pair[0]] = (
                    instruction_pair[0],
                    [instruction_swap[instruction_code], instruction_pair[1][1]],
                )
                new_boot = Booter(file_input=None, instructions=new_instructions)
                try:
                    return new_boot.execute_instruction()
                except InfiniteLoopError:
                    pass
        return 0, 0


class InfiniteLoopError(Exception):
    """
    Exception raised when an infinite loop is entered.

    Attributes:
        accumulator -- value of accumulator before error
        message -- explanation of the error
    """

    def __init__(self, accumulator):
        self.accumulator = accumulator
        self.message = f"About to enter infinite loop. Accumulator value: {accumulator}"
        super().__init__(self.message)
