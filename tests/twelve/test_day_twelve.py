from twelve.twelve import NavSystem


def test_nav_system():
    nav = NavSystem(
        "/home/jonathan/projects/2020-advent-of-code/tests/twelve/part-one-test-one.txt"
    )
    nav.execute()
    assert nav.manhattan_distance() == 25
    assert nav._current_facing == "W"


def test_nav_with_entire():
    nav = NavSystem()
    nav.execute()
    assert nav.manhattan_distance() == 0
