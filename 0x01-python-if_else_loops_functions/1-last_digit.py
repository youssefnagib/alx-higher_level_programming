#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last = abs(number) % 10
if number < 0:
    Last = -Last
    print(f"Last digit of {number:d} is {Last:d} and is less than 6 and not 0")
elif Last == 0:
    print("Last digit of {} is {} and is 0".format(number, Last))
elif Last > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, Last))
else:
    print(f"Last digit of {number:d} is {Last:d} and is less than 6 and not 0")
