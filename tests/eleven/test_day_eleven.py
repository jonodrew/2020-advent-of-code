from eleven.eleven import GameOfChairs


def test_execute():
    game = GameOfChairs(
        "/home/jonathan/projects/2020-advent-of-code/tests/eleven/one.txt"
    )
    game_five = GameOfChairs(
        "/home/jonathan/projects/2020-advent-of-code/tests/eleven/one-iteration-five.txt"
    )
    game.execute()
    assert game._current_configuration == game_five._current_configuration
    assert game._stable_occupation == 37


def test_iterate():
    game = GameOfChairs(
        "/home/jonathan/projects/2020-advent-of-code/tests/eleven/one.txt"
    )
    game._iterate()
    game_two = GameOfChairs(
        "/home/jonathan/projects/2020-advent-of-code/tests/eleven/one-iteration-two.txt"
    )
    for i in range(game._height):
        print(i)
        assert game._current_configuration[i] == game_two._current_configuration[i]
