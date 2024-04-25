#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_numbers = {'I': 1, 'V': 5, 'X': 10,
                     'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    old = 0
    result = 0

    for ch in reversed(roman_string):
        value = roman_numbers[ch]

        if value < old:
            result = result - value
        else:
            result += value
        old = value
    return result
