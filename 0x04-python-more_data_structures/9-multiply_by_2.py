#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiply_2 = {}
    for key in a_dictionary:
        multiply_2[key] = a_dictionary[key] * 2
    return multiply_2
