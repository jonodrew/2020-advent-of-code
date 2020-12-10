from ten.ten import DayTen
import pytest


@pytest.mark.parametrize(
    "example, expected_diffs_1_3, expected_product, total_combinations",
    [
        (
            "/home/jonathan/projects/2020-advent-of-code/tests/ten/one-two.txt",
            (22, 10),
            220,
            19208,
        ),
        (
            "/home/jonathan/projects/2020-advent-of-code/tests/ten/test-ten-one-one.txt",
            (7, 5),
            35,
            8,
        ),
    ],
)
def test_jolt_difference(
    example, expected_diffs_1_3, expected_product, total_combinations
):
    d = DayTen(example)
    d.execute()
    assert d.joltage_differences[1], d.joltage_differences[3] == expected_diffs_1_3
    assert d.jolts_multiplied([1, 3]) == expected_product
    assert d.total_combinations() == total_combinations
