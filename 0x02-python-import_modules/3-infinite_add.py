#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    i = 1
    total = 0
    for i in range(i, argc + 1):
        total = total + int(sys.argv[i])
    print("{}".format(total))
