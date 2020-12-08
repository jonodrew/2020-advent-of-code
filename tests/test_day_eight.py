from eight.eight import Booter, InfiniteLoopError, DayEight
import pytest


def test_day_eight():
    b = Booter("/home/jonathan/projects/2020-advent-of-code/tests/test-eight.txt")
    with pytest.raises(InfiniteLoopError) as exception_info:
        b.execute_instruction()
    assert exception_info.value.accumulator == 5


def test_day_eight_part_two():
    d = DayEight("/home/jonathan/projects/2020-advent-of-code/tests/test-eight.txt")
    assert d.fix_by_trial_and_error() == (0, 8)
