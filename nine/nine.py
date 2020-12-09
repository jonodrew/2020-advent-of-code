from helpers import ReadLines
from typing import List, Union


class UnencryptedDataError(Exception):
    def __init__(self, error_value: int):
        self.message = f"This piece of data is unencrypted: {error_value}"
        super(UnencryptedDataError, self).__init__(self.message)


class Haxx(ReadLines):
    def __init__(self, file_input=None, preamble: int = 25):
        super(Haxx, self).__init__(file_input, "nine")
        self.haxx_inputs: List[int] = [int(value) for value in self.inputs]
        self._preamble: int = preamble
        self._working_values: List[int] = [
            self.haxx_inputs[i] for i in range(self._preamble)
        ]
        self._current_sums: List[Union[int, None]] = [
            value
            for sub_list in [
                self._generate_sum_of_x(self.haxx_inputs[i])
                for i in range(self._preamble)
            ]
            for value in sub_list
        ]

    def _check_number(self, number_index: int = 5) -> bool:
        if self.haxx_inputs[number_index] in self._current_sums:
            return True
        else:
            raise UnencryptedDataError(self.haxx_inputs[number_index])

    def _generate_sum_of_x(self, x: int) -> List[Union[int, None]]:
        return [x + value if value != x else None for value in self._working_values]

    def _remove_old_sums(self):
        self._current_sums = self._current_sums[self._preamble :]

    def find_unencrypted_value(self) -> Union[str, None]:
        for i in range(self._preamble, len(self.haxx_inputs)):
            try:
                self._check_number(i)
            except UnencryptedDataError as e:
                return e.message
            self._remove_old_sums()
            self._working_values.pop(0)
            self._working_values.append(self.haxx_inputs[i])
            self._current_sums.extend(self._generate_sum_of_x(self.haxx_inputs[i]))
        return None
