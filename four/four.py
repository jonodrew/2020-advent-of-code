from typing import List, Dict, Any, Union, Callable
from helpers import AdventOfCodeHelpers
import re


class Passport(object):
    def __init__(self, kwargs: Dict[str, Any]):
        self.fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        for field in self.fields:
            self.__setattr__(field, kwargs.get(field, None))

    @classmethod
    def process_unstructured_data(cls, data: List[str]) -> "Passport":
        passport_data = {
            attribute[0]: attribute[1]
            for attribute in [item.split(":") for item in " ".join(data).split(" ")]
        }
        return Passport(passport_data)


class Validator(object):
    def __init__(self, valid_fields: List[str], strict: bool = False):
        self.valid_fields = valid_fields
        self.validator_function_dict: Dict[str, Callable] = {
            "byr": lambda x: 2002 >= int(x) >= 1920,
            "iyr": lambda x: 2020 >= int(x) >= 2010,
            "eyr": lambda x: 2030 >= int(x) >= 2020,
            "hgt": lambda x: (
                len(x) == 4 and x[-2:] == "in" and 76 >= int(x[0:2]) >= 59
            )
            or (len(x) == 5 and x[-2:] == "cm" and 193 >= int(x[0:3]) >= 150),
            "hcl": re.compile(r"^#[a-z0-9]{6}").match,
            "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
            "pid": re.compile(r"^\d{9}$").match,
        }
        self.strict = strict

    def validate_passport(self, passport: Passport) -> bool:
        for field in self.valid_fields:
            field_value = passport.__getattribute__(field)
            if field_value is None:
                return False
            if self.strict:
                if not self.validator_function_dict.get(field, type)(field_value):
                    return False
        return True


class DayFour(AdventOfCodeHelpers):
    def __init__(
        self,
        valid_fields=("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"),
        file_input=None,
    ):
        super().__init__(file_input, day="four")
        self.passports = [
            Passport.process_unstructured_data(data) for data in self._group()
        ]
        self.validator = Validator(valid_fields)
        self.valid_passport_count = self.valid_passports()

    def valid_passports(self):
        return [self.validator.validate_passport(p) for p in self.passports].count(True)

    def strict_valid_passports(self) -> int:
        self.validator.strict = True
        return self.valid_passports()
