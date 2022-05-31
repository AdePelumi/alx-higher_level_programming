#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = str(number)
print(f"Last digit of {number:d} is {int(last_digit[-1]):d}", end=" ")

if int(last_digit[-1]) > 5:
    print("and is greater than 5")
elif int(last_digit[-1]) == 0:
    print(f"and is {0:d}")
elif int(last_digit[-1]) < 6:
    print("and is less than 6 and not 0")
