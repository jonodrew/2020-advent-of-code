from six.six import DaySix, PartOne, PartTwo
import pytest


def test_group():
    d = DaySix("/home/jonathan/projects/2020-advent-of-code/tests/test-six.txt")
    assert d._group() == [
        ["abc"],
        ["a", "b", "c"],
        ["ab", "ac"],
        ["a", "a", "a", "a"],
        ["b"],
    ]


def test_part_one():
    p = PartOne("/home/jonathan/projects/2020-advent-of-code/tests/test-six.txt")
    assert p.sum_of_counts == 11


class TestPartTwo:
    def test_part_two_all_yeses(self):
        p = PartTwo("/home/jonathan/projects/2020-advent-of-code/tests/test-six.txt")
        assert p.sum_of_counts == 6

    @pytest.mark.parametrize(
        "group_answers, count", [(["abc"], 3), (["a", "b", "c"], 0), (["ab", "ac"], 1)]
    )
    def test_part_two_under_all_yeses(self, group_answers, count):
        assert PartTwo._yeses_in_group(group_answers) == count
