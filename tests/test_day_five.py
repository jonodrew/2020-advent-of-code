from five.five import DayFive
import pytest


@pytest.mark.parametrize(
    "input, row, column, id",
    [
        ("BFFFBBFRRR", 70, 7, 567),
        ("FFFBBBFRRR", 14, 7, 119),
        ("BBFFBBFRLL", 102, 4, 820),
    ],
)
def test_identify_seat(input, row, column, id):
    d = DayFive()
    assert (row, column, id) == d.identify_seat(input)
