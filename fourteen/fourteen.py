from helpers import ReadLines
from typing import Dict, List


class DockingData(ReadLines):
    def __init__(self, file_input=None):
        super(DockingData, self).__init__("fourteen", file_input)
        self._mask: Dict[int, str] = {}
        self._memory: Dict[int, str] = {0: "000000000000000000000000000000000000"}

    def execute(self):
        for instruction in self.inputs:
            if instruction[:4] == "mask":
                self.mask = instruction[7:]
            else:
                self._process_memory_write(instruction)
        return None

    def sum_values_in_memory(self) -> int:
        return sum((int(value, 2) for value in self._memory.values()))

    def _apply_mask(self, value: str) -> str:
        value_as_list = list(value)
        for bit_position, bit_value in enumerate(value_as_list):
            masked_bit = self._mask.get(bit_position, None)
            if masked_bit is None:
                pass
            else:
                value_as_list[bit_position] = masked_bit
        return "".join(value_as_list)

    def _process_memory_write(self, instruction: str):
        instructions: List[str] = instruction.split("=")
        location: int = int(instructions[0].rstrip()[4:-1])
        value: str = format(int(instructions[1].rstrip()), "036b")
        new_value: str = self._apply_mask(value)
        self._memory[location] = new_value

    @property
    def mask(self):
        return self._mask

    @mask.setter
    def mask(self, value: str):
        new_mask = {}
        for i, bit in enumerate(value):
            if bit in {"0", "1"}:
                new_mask[i] = bit
        self._mask = new_mask
