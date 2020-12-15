from fifteen.fifteen import Recitation
import pytest


@pytest.mark.parametrize(
    "puzzle_input, expected_output",
    [
        ([1, 3, 2], 1),
        ([2, 1, 3], 10),
        ([1, 2, 3], 27),
        ([2, 3, 1], 78),
        ([3, 2, 1], 438),
        ([3, 1, 2], 1836),
        ([0, 3, 6], 436),
    ],
)
def test_recitation(puzzle_input, expected_output):
    r = Recitation(puzzle_input)
    assert r.execute() == expected_output
