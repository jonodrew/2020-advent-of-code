from three.main import DayThree, NoMoveError
import pytest


class TestDayThree:
    @pytest.mark.parametrize(
        "start_position, end_position", [((0, 0), (1, 3)), ((0, 30), (1, 2))]
    )
    def test_move(self, start_position, end_position):
        d = DayThree("tests/test-three-one.txt")
        assert end_position == d.move(start_position)

    def test_move_errors_when_at_bottom(self):
        d = DayThree("tests/test-three-one.txt")
        with pytest.raises(NoMoveError):
            d.move((1, 0))
