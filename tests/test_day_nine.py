from nine.nine import Haxx
import pytest


@pytest.fixture
def test_haxx():
    h = Haxx(
        "/home/jonathan/projects/2020-advent-of-code/tests/test-nine.txt", preamble=5
    )
    return h


class TestHaxx:
    def test_find_unencrypted_data(self, test_haxx):
        assert (
            test_haxx.find_unencrypted_value()
            == "This piece of data is unencrypted: 127"
        )

    def test_find_weakness(self, test_haxx):
        assert test_haxx.find_weakness() == 62
