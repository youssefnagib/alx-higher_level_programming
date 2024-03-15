#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = 0
    if 1 == len(sys.argv):
        print("0 arguments.")
    elif 2 == len(sys.argv):
        print("1 argument:")
    else:
        n = len(sys.argv) - 1
        print("{} arguments:".format(n))
    for i in sys.argv[1:]:
        num += 1
        print("{}: {}".format(num, i))
