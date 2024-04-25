#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    def number_1(n):
        return n * number  
    return list(map(number_1, my_list))
