#!/usr/bin/python3
for b in range(90, 64 , -1):
    print(chr(b + 32) if b % 2 == 0 else chr(b),end="")
