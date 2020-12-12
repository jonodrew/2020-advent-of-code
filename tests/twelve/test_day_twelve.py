from twelve.twelve import Ship, ShipWithWayPoint


def test_nav_system():
    s = Ship(
        file_input="/home/jonathan/projects/2020-advent-of-code/tests/twelve/part-one-test-one.txt"
    )
    s.execute()
    assert s.manhattan_distance() == 25
    assert s.current_facing == "W"


def test_part_two():
    s = ShipWithWayPoint(
        file_input="/home/jonathan/projects/2020-advent-of-code/tests/twelve/part-one-test-one.txt"
    )
    s.execute()
    assert s.manhattan_distance() == 286
