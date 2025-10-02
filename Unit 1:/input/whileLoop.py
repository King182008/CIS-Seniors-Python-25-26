''''
File: While Loop
Class: CIS Seniors
Name: Xaiden Morey
Date: 10/2/2025

set the sum to 0.0
input the string
while the string is not the empty string
    conert the string to a float
    add the float to the sum
    input a string
print the sum

Loop Control Variable - the first input statement that initializes a variable to a value that the loop conidtion can test.
'''

theSum = 0.0
data = input("Enter a number or just enter to quit: ")
while data != "":
    number = float(data)
    theSum += number
    data = input("Enter a number or just enter to quit: ")

print("The sum is:", theSum)

print("\n\nA count-controlled while Loop")

# Sumnation with a for loop
theSum = 0
for count in range(1, 10001):
    theSum += count

print(theSum, "\n\n")

# Sumnation with a while loop
theSum = 0
count = 1
while count <= 10000:
    theSum += count
    count += 1

print(theSum)


print("\n\nCounting down with loops.")
# Counting down with a for loop
for count in range(10, 0, -1):
    print(count, end=" ")

# Counting down with a while loop 
count = 10
while count >= 1:
    print(count, end=" ")
    count -= 1

print("\n\nThe while True Statement with a break statement")

theSum = 0.0
while True:
    data = input("Enter a number or just enter to quit: ")  # Set control variable
    if data == "":   # Termination condition
        break   # The break statement will end the loop
    number = float(data)
    theSum += number
print("The sum is", theSum)

print("\n\nGrading Example:\n")
while True:
    number = int(input("Enter the numeric grade: "))
    if number >= 0 and number <= 100:
        break
    else:
        print("Error: grade must be between 100 and 0")

print (number) # just echo the valid input

print("\n\nDifferent Grading Example\n")
done = False
while not done:      # while not == dalse
    number = int(input("Enter a numeric grade: "))
    if number  >= 0 and number <= 100:
        done = True:
    else:
        print("Error: grade must be between 100 and 0.")
print(number)