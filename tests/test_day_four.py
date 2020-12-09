from four.four import DayFour
import pytest


class TestDayFour:
    def test_valid_passports(self):
        d = DayFour(
            file_input="/home/jonathan/projects/2020-advent-of-code/tests/test-four-one.txt"
        )
        assert d.valid_passports() == 2


def test_entire():
    d = DayFour()
    assert d.valid_passport_count == 228


@pytest.mark.parametrize(
    "file_path, expected",
    (
        (
            "/home/jonathan/projects/2020-advent-of-code/tests/test-four-two-valid.txt",
            4,
        ),
        (
            "/home/jonathan/projects/2020-advent-of-code/tests/test-four-two-invalid.txt",
            0,
        ),
        ("/home/jonathan/projects/2020-advent-of-code/four/input.txt", 175),
    ),
)
def test_entire_strict(file_path, expected):
    d = DayFour(file_input=file_path)
    assert d.strict_valid_passports() == expected
