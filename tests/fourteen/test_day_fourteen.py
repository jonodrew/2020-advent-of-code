from fourteen.fourteen import DockingData


def test_docking_data():
    d = DockingData("tests/fourteen/part-one.txt")
    d.execute()
    assert d.sum_values_in_memory() == 165
