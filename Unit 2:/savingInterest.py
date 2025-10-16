'''
An Example of using math module to calculate the interest of a saving account
'''

import math

base = float(input("Enter initial savings: "))
print()

rate = float(input("Enter annual interest rate: "))
print()

years = int(input("Enter total years passed: "))
print()

total = base * math.pow(1 + (rate / 100), years)
print(f"Savings after {years} years is ${total:.2f}")