from thirteen.thirteen import ShuttleSearch, Bus


class TestShuttle:
    def test_input(self):
        shuttle = ShuttleSearch(
            "/home/jonathan/projects/2020-advent-of-code/tests/thirteen/part-one.txt"
        )
        assert shuttle._departure_time == 939
        assert shuttle._buses == [7, 13, 59, 31, 19]

    def test_calculate(self):
        shuttle = ShuttleSearch(
            "/home/jonathan/projects/2020-advent-of-code/tests/thirteen/part-one.txt"
        )
        assert shuttle.bus_times_wait() == 295

    def test_offset(self):
        shuttle = ShuttleSearch(
            "/home/jonathan/projects/2020-advent-of-code/tests/thirteen/part-one.txt"
        )
        assert shuttle.offset_buses().offset == 1068781

    def test_real(self):
        shuttle = ShuttleSearch()
        assert shuttle.offset_buses().offset == 905694340256752

    def test_pair(self):
        shuttle = ShuttleSearch()
        bus = shuttle.paired_bus_intervals(Bus(3, 0), Bus(5, 1))
        assert bus.offset == 9
