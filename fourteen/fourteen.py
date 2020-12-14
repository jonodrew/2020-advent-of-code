from helpers import ReadLines
from typing import Dict, List, Tuple, Callable
import itertools


class DockingData(ReadLines):
    def __init__(self, file_input=None):
        super(DockingData, self).__init__(day="fourteen", file_input=file_input)
        self._mask: Dict[int, str] = {}
        self._memory: Dict[int, str] = {0: "000000000000000000000000000000000000"}
        self._pass_bit_rule: Callable = lambda x: x == ""

    def execute(self):
        for instruction in self.inputs:
            if instruction[:4] == "mask":
                self.mask = instruction[7:]
            else:
                self.process_memory_write(instruction)
        return None

    def sum_values_in_memory(self) -> int:
        return sum((int(value, 2) for value in self._memory.values()))

    def _apply_mask(self, value: str) -> str:
        value_as_list = list(value)
        for bit_position, bit_value in enumerate(value_as_list):
            masked_bit = self._mask.get(bit_position, "")
            if not self._pass_bit_rule(masked_bit):
                value_as_list[bit_position] = masked_bit
        return "".join(value_as_list)

    def process_memory_write(self, instruction: str):
        location, value = self._extract_instructions(instruction)
        value_as_binary = self._convert_to_binary_string(value)
        new_value: str = self._apply_mask(value_as_binary)
        self._write_to_memory(location, new_value)

    def _write_to_memory(self, location: int, value: str):
        self._memory[location] = value

    @staticmethod
    def _extract_instructions(instruction) -> Tuple[int, int]:
        instructions = [instruction.strip() for instruction in instruction.split("=")]
        return int(instructions[0][4:-1]), int(instructions[1])

    @staticmethod
    def _convert_to_binary_string(value: int) -> str:
        return format(value, "036b")

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


class VersionTwo(DockingData):
    def __init__(self, file_input=None):
        super(VersionTwo, self).__init__(file_input)
        self._pass_bit_rule: Callable = lambda x: x == "" or x == "0"

    def process_memory_write(self, instruction: str):
        location, value = self._extract_instructions(instruction)
        location_as_binary = self._convert_to_binary_string(location)
        new_location_address: str = self._apply_mask(location_as_binary)
        new_locations = self._generate_new_memory_addresses(new_location_address)
        for new_location in new_locations:
            self._write_to_memory(
                int(new_location, 2), self._convert_to_binary_string(value)
            )

    def _generate_new_memory_addresses(self, floating_address: str) -> List[str]:
        as_list = list(floating_address)
        indices_of_floating_bits = [
            i for i, letter in enumerate(as_list) if letter == "X"
        ]
        number_of_floating_bits = len(indices_of_floating_bits)
        combos = list(itertools.product(range(2), repeat=number_of_floating_bits))
        addresses = [as_list.copy() for i in combos]
        for i, combo in enumerate(combos):
            for j, value in enumerate(indices_of_floating_bits):
                addresses[i][value] = str(combo[j])
        return ["".join(address) for address in addresses]

    @property
    def mask(self):
        return super()._mask

    @mask.setter
    def mask(self, value):
        new_mask = {}
        for i, bit in enumerate(value):
            new_mask[i] = bit
        self._mask = new_mask
