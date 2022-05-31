#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = str(number)[-1]
last = -int(last) if number < 0 else int(last) 
print(f"Last digit of {number} is {last if number < 0 and last !=0 else last } {'and is greater than 5' if last > 5 else ''} {'and is 0' if last == 0 else ''} {'and is less than 6 and not 0' if last < 6 and last != 0 else ''}")