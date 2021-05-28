from seventeen.seventeen import Space, Cube
import pytest


class TestCubes:
    def test_init(self):
        """
        .#.
        ..#
        ###
        """
        model = Space("seventeen/test-input-one.txt")
        assert model.find_cube(0, 0, 0) == Cube([0, 0, 0], True)
        assert model.find_cube(0, 2, 0) == Cube([0, 2, 0], False)

    @pytest.mark.parametrize(
        ["iterations", "active_cubes"],
        [
            (
                0,
                5,
            ),
            (
                1,
                11,
            ),
            (
                2,
                21,
            ),
            (3, 38),
            (6, 112),
        ],
    )
    def test_iterate(self, iterations, active_cubes):
        model = Space("seventeen/test-input-one.txt")
        for i in range(iterations):
            model.iterate()
        assert len([cube for cube in model.cubes if cube.state]) == active_cubes
