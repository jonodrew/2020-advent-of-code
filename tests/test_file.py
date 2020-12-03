from three.main import DayThree
import pytest


class TestDayThree:
    @pytest.mark.parametrize("start_position, end_position", [((0, 0), (1, 3))])
    def test_move(self, start_position, end_position):
        d = DayThree("tests/test-three-one.txt")
        assert end_position == d.move(start_position)
