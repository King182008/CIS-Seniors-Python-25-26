'''
File Name: input.py
Name: Xaiden Morey
Class: CIS Seniors
Date: 9/19/20225
'''

firstName = input("Enter your fisrt name: ")
lastName = input("Enter your last name: ")
age = input("How old are you? ")
math = input("What is pi? ")
favorite = input("Is this your favorite class? ")

print("\n\n\n")
print("Your name is " + firstName + " " + lastName + ".")
print("You are " + age + " years old.")
print("You know that pi is " + math + ".")

if favorite == "yes":
    favorite = "True"
    print("I am happy to hear this is your favorite class!")
else:
    favorite = "False" 
    print("You suck, leave!")
print("\n\n\n")