from helpers import ReadLines
import re


class Deducter(ReadLines):
    def __init__(self, file_input=None):
        super(Deducter, self).__init__('sixteen', file_input=file_input)
        self.error_rate = 0
        self.good_tickets = []
        self.fields = {}

        split_input = self.split_input()
        self.rules_as_text = split_input[0]
        self.my_ticket_values = [int(v) for v in split_input[1][1].split(',')]
        self.other_ticket_values = split_input[2][1:]
        self.rules = self.read_rules_to_dict()

    def process(self):
        self.collect_good_tickets()
        self.fields = self.deducer()


    def split_input(self):
        space_indices = [i for i, string in enumerate(self.inputs) if string == '']
        space_indices.append(len(self.inputs))
        output = []
        start = 0
        for i, index in enumerate(space_indices):
            output.append(self.inputs[start:space_indices[i]])
            start = space_indices[i]+1
        return output

    def read_rules_to_dict(self) -> dict[str, list[int]]:
        rules = {}
        for rule in self.rules_as_text:
            rule_name = rule[0: rule.index(':')]
            rule_as_text = rule[rule.index(':')+2:]
            values_regex = re.compile(r'(\d+-\d+)+')
            values = values_regex.findall(rule_as_text)
            min_max = []
            for value in values:
                value_regex = re.compile(r'\d+')
                values = [int(v) for v in value_regex.findall(value)]
                min_max.extend(values)
            rules[rule_name] = min_max
            self.fields[rule_name] = None
        return rules

    def collect_good_tickets(self):
        good_tickets = []
        for ticket in self.other_ticket_values:
            values = ticket.split(',')
            ticket = [int(v) for v in values]
            try:
                self.check_good_ticket(ticket)
                good_tickets.append(ticket)
            except BadTicketError as e:
                self.error_rate += e.value
        self.good_tickets = good_tickets


    def check_good_ticket(self, ticket: list[int]):
        for value in ticket:
            valid_against_one_rule = any((self.check_against_rule(value, rule) for rule in self.rules.values()))
            if not valid_against_one_rule:
                raise BadTicketError(value)
        return 0

    def check_against_rule(self, value: int, rule: list[int]):
        return rule[0] <= value <= rule[1] or rule[2] <= value <= rule[3]

    def classifier(self):
        number_of_fields = len(self.good_tickets[0])
        potential_fields = {i: [] for i in range(number_of_fields)}
        same_fields = [[ticket[i] for ticket in self.good_tickets] for i in range(number_of_fields)]
        for i, field in enumerate(same_fields):
            for name, rule in self.rules.items():
                if all(self.check_against_rule(value, rule) for value in field):
                    potential_fields[i].append(name)
        return potential_fields

    def deducer(self):
        potential_fields = self.classifier()
        real_fields = {}
        while not len(real_fields.values()) == len(self.my_ticket_values):
            for position, options in potential_fields.items():
                if len(options) == 1:
                    only_solution = options[0]
                    real_fields[position] = only_solution
                    potential_fields = {position: [option for option in options if option != only_solution] for position, options in potential_fields.items()}
                    potential_fields.pop(position)
                    break
                else:
                    pass
        return real_fields

    def multiply_values(self, key_string: str=None):
        self.process()
        product = 1
        for position, name in self.fields.items():
            if (key_string and key_string in name) or not key_string:
                print(self.my_ticket_values[position])
                product *= self.my_ticket_values[position]
        return product


class BadTicketError(BaseException):
    def __init__(self, bad_value: int):
        self.value = bad_value
        self.message = "Ticket has an invalid field"


def main():
    d = Deducter()
    print(d.multiply_values('departure'))
    print(d.fields.items())

    print(d.error_rate)


if __name__ == '__main__':
    main()
