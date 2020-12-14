from fourteen.fourteen import DockingData, VersionTwo


def test_docking_data():
    d = DockingData("tests/fourteen/part-one.txt")
    d.execute()
    assert d.sum_values_in_memory() == 165


def test_part_two():
    d = VersionTwo(file_input="tests/fourteen/part-two.txt")
    d.execute()
    assert d.sum_values_in_memory() == 208
