#!/usr/bin/python3
import sys
num = 0
if 1 == len(sys.argv):
    print("0 arguments.")
else:
    n = len(sys.argv) - 1
    print("{} arguments:".format(n))
    for i in sys.argv[1:]:
        num += 1
        print("{}: {}".format(num, i))
