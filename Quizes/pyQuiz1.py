'''
File: Python Quiz 1 
Name: Xaiden Morey
Class: CIS Seniors
Date: 10/1/2025
'''

print("Question 1")
for count in range(0, 6):
    print(count)

print("=" * 40)
print("Question 2")

for count in range(3, 9):
    print(count)

print("=" * 40)
print("Question 3")

for count in range(0, 11, 2):
    print(count)

print("=" * 40)
print("Question 4")

for count in range(10, 0, -1):
    print(count)

print("=" * 40)
print("Question 5")

for count in range(1, 6):
    print("5 x", count, "=", (count * 5))

print("=" * 40)
print("Question 6")

age = int(input("Please enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor")

print("=" * 40)
print("Question 7")

for count in range(0, 10):
    if count % 2:
        print("Even")
    else:
        print("Odd")

print("=" * 40)
print("Question 8")

for count in range(20, -1, -5):
    print("Countdown:", count)

print("=" * 40)
print("Question 9")

for count in range(1, 7):
    if count <= 3:
        print("Number", count, "is Small")
    else:
        print("Number", count, "is Large")

print("=" * 40)
print("Question 10")

userNumber = int(input("please enter a number: "))
for count in range(1, userNumber + 1, 2):
    if count < 5:
        print("Low:", count)
    else:
        print("High:", count)

print("=" * 40)
print("Bonus Question")

for count in range(15, -1, -3):
    if count == 0:
        print("Blastoff!")
    else:
        print(count)