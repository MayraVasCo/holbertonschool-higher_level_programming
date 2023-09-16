#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
stringtonumber = str(number)
ultimo_numero = int(stringtonumber[-1])

if ultimo_numero > 5:
    print(f"Last digit of {number} is {ultimo_numero} and is greater than 5")

elif ultimo_numero == 0:
    print(f"Last digit of {number} is {ultimo_numero} and is 0")

elif ultimo_numero < 6 and ultimo_numero != 0:
    print(f"Last digit of {number} is {ultimo_numero} and is less than 6 and not 0")
