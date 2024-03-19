#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    tuple_1a = tuple_a + (0, 0)
    tuple_1b = tuple_b + (0, 0)
    new_tuple = tuple_1a[0] + tuple_1b[0], tuple_1a[1] + tuple_1b[1]
    return new_tuple
