import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from sample_proj.pandas_csv.nato_phonetic.nato_phonetic_app.nato_phonetic_parser import boot_strup, parser

@pytest.mark.parametrize('actual, expected',
                         [('My flight departs soon',
                           ['Mike', 'Yankee', 'Foxtrot', 'Lima', 'India', 'Golf', 'Hotel', 'Tango', 'Delta', 'Echo', 'Papa', 'Alpha', 'Romeo', 'Tango', 'Sierra', 'Sierra', 'Oscar', 'Oscar', 'November']),
                          ('1 2 3 4', ['One', 'Two', 'Three', 'Four'])])
def test_correct_conversion_words(actual, expected):
    boot_strup()

    parser_return = parser(actual.upper())

    assert parser_return==expected