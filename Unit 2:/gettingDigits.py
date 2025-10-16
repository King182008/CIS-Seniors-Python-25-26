'''
file: Getting Digits
Name: Xaiden Morey
Date: 10/14/2025
Class: CIS Seniors

Given a number, % and // can be used ti get each digit. For the three-digit number user_val like 927:
'''

myDigit = int(input("Enter a three digit number: "))

oneDigit = myDigit % 10
temp_val = myDigit // 10
print("The ones digit is", oneDigit)

tenDigit = temp_val % 10
temp_val = temp_val // 10
print("The tens place is", tenDigit)

hundredsDigit = temp_val % 10
print("The hundreds place is", hundredsDigit)