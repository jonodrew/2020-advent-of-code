from seven.seven import BagOfHolding, DaySeven
import pytest


class TestBagOfHolding:
    @pytest.mark.parametrize(
        "rule, output",
        [
            (
                "light red bags contain 1 bright white bag, 2 muted yellow bags.",
                ("light red", [(1, "bright white"), (2, "muted yellow")]),
            ),
            ("dotted black bags contain no other bags.", ("dotted black", [])),
        ],
    )
    def test_process_rule(self, rule, output):
        b = BagOfHolding(rule)
        assert b.process_rule(b.rule_as_string) == output

    @pytest.mark.parametrize(
        "bag_colour, bags_within",
        [("dark violet", 0), ("shiny gold", 126), ("dark blue", 2)],
    )
    def test_number_of_bags_required(self, bag_colour, bags_within):
        d = DaySeven(
            "/home/jonathan/projects/2020-advent-of-code/tests/test-seven-two.txt"
        )
        bag = d.all_bags.get(bag_colour)
        assert bag.bags_to_buy() == bags_within


class TestDaySeven:
    def test_bag_factory(self):
        d = DaySeven("/home/jonathan/projects/2020-advent-of-code/tests/test-seven.txt")
        assert len(d.all_bags.items()) == 9

    @pytest.mark.parametrize(
        "bag, may_contain",
        [
            ("bright white", True),
            ("dark orange", True),
            ("light red", True),  # Muted yellow can contain shiny gold
            ("shiny gold", False),
            ("dotted black", False),
        ],
    )
    def test_may_contain(self, bag, may_contain):
        d = DaySeven("/home/jonathan/projects/2020-advent-of-code/tests/test-seven.txt")
        assert d.all_bags[bag].may_contain is may_contain
