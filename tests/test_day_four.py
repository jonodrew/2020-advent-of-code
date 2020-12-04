from four.main import *
import pytest


class TestPassport(object):
    @pytest.mark.parametrize(
        "field, value,output_value", [
            ('ecl', 'blue', None), ('ecl', 'blu', 'blu'), ('hcl', '123abc', None), ('hcl', '#123abc', '#123abc'), ('iyr', '2011', 2011), ('byr', '1990', 1990),
            ('hgt', '160cm', '160cm'), ('hgt', '190', None), ('pid', '00000000', None), ('pid', '0123456789', None)
        ]
    )
    def test_setters(self, field, value, output_value):
        p = Passport({field: value})
        assert p.__getattribute__(field) == output_value
