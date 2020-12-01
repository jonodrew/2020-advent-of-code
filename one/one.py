from functools import reduce 
import operator
from itertools import product


class DayOne(object):
    def __init__(self):
        with open('one/input.txt', 'r') as reader:
            self.expenses = [int(line) for line in reader]
    
    def sum_to_value(self, number_to_sum=2, sought_value=2020):
        lists = [self.expenses]*number_to_sum
        pairs = product(*lists)
        for pair in pairs:
            if sum(pair) == 2020:
                return self.prod(pair)
                break

    @classmethod
    def prod(cls, iterable):
        return reduce(operator.mul, iterable, 1)
    
d = DayOne()
print(d.sum_to_value())
one_two = d.sum_to_value(number_to_sum=3)
print(one_two)
    