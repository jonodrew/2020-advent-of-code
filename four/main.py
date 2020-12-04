from typing import List, Dict, Any
from helpers import ReadLines
import re
from typing import Union


class Passport(object):
    def __init__(self, kwargs: Dict[str, Any]):
        self.fields = [('byr', 0), ('iyr', 0), ('eyr', 0), ('hgt', '00ab'), ('hcl', ''), ('ecl', ''), ('pid', ''), ('cid', '')]
        for field in self.fields:
            self.__setattr__(f'_{field[0]}', None)
            self.__setattr__(field[0], kwargs.get(field[0], field[1]))

    @staticmethod
    def _value_validator(value: str, max: int, min: int) -> Union[int, None]:
        value = int(value)
        if max >= value >= min:
            return value
        else:
            return None

    @property
    def byr(self):
        return self._byr

    @byr.setter
    def byr(self, value):
        self._byr = self._value_validator(value, 2002, 1920)

    @property
    def iyr(self):
        return self._iyr

    @iyr.setter
    def iyr(self, value):
        self._iyr = self._value_validator(value, 2020, 2010)

    @property
    def eyr(self):
        return self._eyr

    @eyr.setter
    def eyr(self, value):
        self._eyr = self._value_validator(value, 2030, 2020)

    @property
    def hgt(self):
        return self._hgt

    @hgt.setter
    def hgt(self, value):
        if len(value) < 4 or len(value) > 5:
            self._hgt = None
        else:
            units = value[-2:]
            number = int(value[:-2])
            if (units == 'in' and 76>=number>=59) or (units == 'cm' and 193>=number>=150):
                self._hgt = value
            else:
                self._hgt = None

    @property
    def hcl(self):
        return self._hcl

    @hcl.setter
    def hcl(self, value):
        expression = re.compile('^#[a-z0-9]{6}')
        self._hcl = value if expression.match(value) else None

    @property
    def ecl(self):
        return self._ecl

    @ecl.setter
    def ecl(self, value):
        self._ecl = value if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] else None

    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        expression = re.compile('^\d{9}$')
        self._pid = value if expression.match(value) else None

    @classmethod
    def process_unstructured_data(cls, data: List[str]) -> 'Passport':
        passport_data = {attribute[0]: attribute[1] for attribute in [item.split(':') for item in ' '.join(data).split(' ')]}
        return Passport(passport_data)


class Validator(object):
    def __init__(self, valid_fields: List[str]):
        self.valid_fields = valid_fields

    def validate_passport(self, passport: Passport) -> bool:
        for field in self.valid_fields:
            if passport.__getattribute__(field) is None:
                return False
        return True


class DayFour(ReadLines):
    def __init__(self, path_to_input='four/input.txt', valid_fields=('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')):
        super().__init__(path_to_input)
        self.passports = self.process_passport_data()
        self.validator = Validator(valid_fields)
        self.valid_passport_count = 0

    def process_passport_data(self):
        passports = []
        data = []
        for line in self.inputs:
            if line == '':
                passports.append(Passport.process_unstructured_data(data))
                data = []
            else:
                data.append(line)
        return passports

    def valid_passports(self):
        self.valid_passport_count = [self.validator.validate_passport(p) for p in self.passports].count(True)
