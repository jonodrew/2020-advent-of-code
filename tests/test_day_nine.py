from nine.nine import Haxx
import pytest


class TestHaxx:
    def test_find_unencrypted_data(self):
        h = Haxx(
            "/home/jonathan/projects/2020-advent-of-code/tests/test-nine.txt",
            preamble=5,
        )
        assert h.find_unencrypted_value() == "This piece of data is unencrypted: 127"
