from sixteen.sixteen import Deducter, BadTicketError
import pytest


@pytest.fixture()
def deducter_one():
    return Deducter(file_input='tests/sixteen/test_input.txt')

@pytest.fixture()
def deducter_two():
    return Deducter(file_input='tests/sixteen/test-input-two.txt')

class TestDeducter:
    def test_rule_reader(self, deducter_one):
        d = deducter_one
        assert d.check_good_ticket([7, 3, 47]) == 0
        with pytest.raises(BadTicketError):
            d.check_good_ticket([40, 4, 50])
            d.check_good_ticket([55, 2, 20])
            d.check_good_ticket([38, 6, 12])

    def test_collect_good_tickets(self, deducter_one):
        deducter_one.collect_good_tickets()
        assert deducter_one.error_rate == 71

    def test_deducer(self, deducter_two):
        deducter_two.collect_good_tickets()
        classfiers = deducter_two.deducer()
        assert classfiers == {
            0: 'row',
            1: 'class',
            2: 'seat'
        }

    def test_multiplier(self, deducter_two):
        assert deducter_two.multiply_values() == 1716
