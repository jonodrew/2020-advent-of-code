from helpers import AdventOfCodeHelpers
import re
from typing import Tuple, List, Dict


class DaySeven(AdventOfCodeHelpers):
    def __init__(self, file_input=None):
        super(DaySeven, self).__init__(file_input=file_input, day="seven")
        self.list_of_bag_rules = [self._process_line(rule) for rule in self.inputs]
        self.all_bags: Dict[str, BagOfHolding] = {}
        while self.inputs:
            self.bag_factory(self.inputs.pop(0))

    def bag_factory(self, line: str, may_contain: str = "shiny gold") -> "BagOfHolding":
        """
        For each rule, there is a parent node and a reference to (n) children. The reference points to a line where the node is fully detailed.
        Therefore we need to iterate over the first line, create the Bag, capture the references, identify the references in the list, and create those Bags,
        etc until we get to a Bag that doesn't have children - and then we can go back to the 2nd line, and so on.
        """
        b = BagOfHolding(line)
        self.all_bags[b.name] = b
        if not b.contains:
            b.may_contain = b.may_contain_bag(may_contain)
            return b
        else:
            for reference in b.contains:
                if reference[1] in self.all_bags:
                    b.bags_within.append(
                        (reference[0], self.all_bags[reference[1]])
                    )  # bag already created
                else:
                    line_index = [
                        " ".join(rule.split(" ")[0:2]) for rule in self.inputs
                    ].index(reference[1])
                    new_line = self.inputs.pop(line_index)
                    b.bags_within.append((reference[0], self.bag_factory(new_line)))
            b.may_contain = b.may_contain_bag(may_contain)
            return b

    @staticmethod
    def _process_line(rule: str,) -> Tuple[str, List[Tuple[int, str]]]:
        name = " ".join(rule.split(" ")[0:2])
        bags_within_regex = re.compile(r"\d\s\w+\s\w+")
        bags = bags_within_regex.findall(rule)
        bags_as_tuples = [
            (int(bag_as_list[0]), " ".join(bag_as_list[1:3]))
            for bag_as_list in [bag.split(" ") for bag in bags]
        ]
        return name, bags_as_tuples


class BagOfHolding(object):
    def __init__(self, rule_as_string: str):
        self.rule_as_string = rule_as_string
        self.name, self.contains = self.process_rule()
        self._may_contain = False
        self.bags_within: List[
            Tuple[int, BagOfHolding]
        ] = []  # number of bags and Bag object
        self._bags_to_buy = 0

    def __repr__(self):
        return self.name

    def process_rule(self) -> Tuple[str, List[Tuple[int, str]]]:
        name = " ".join(self.rule_as_string.split(" ")[0:2])
        bags_within_regex = re.compile(r"\d\s\w+\s\w+")
        bags = bags_within_regex.findall(self.rule_as_string)
        bags_as_tuples = [
            (int(bag_as_list[0]), " ".join(bag_as_list[1:3]))
            for bag_as_list in [bag.split(" ") for bag in bags]
        ]
        return name, bags_as_tuples

    def may_contain_bag(self, requested_bag: str = "shiny gold"):
        if self._may_contain:
            return True
        elif requested_bag in [
            bag.name for bag in [bag_tuple[1] for bag_tuple in self.bags_within]
        ]:
            return True
        elif any(
            [
                bag.may_contain
                for bag in [bag_tuple[1] for bag_tuple in self.bags_within]
            ]
        ):
            return True
        return False

    def bags_to_buy(self) -> int:
        if not self.bags_within:
            return 0
        else:
            return sum(
                [
                    bag_data[0] + bag_data[0] * bag_data[1].bags_to_buy()
                    for bag_data in self.bags_within
                ]
            )

    @property
    def may_contain(self):
        return self._may_contain

    @may_contain.setter
    def may_contain(self, new_value: bool):
        if self._may_contain or new_value:
            self._may_contain = True
        else:
            self._may_contain = False
