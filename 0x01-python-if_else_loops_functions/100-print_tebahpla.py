#!/usr/bin/python3
for b in range(90, 64, -1):
    print("{}".format(chr(b+32))\
            if b % 2 == 0 else "{}".format(chr(b)), end="")
