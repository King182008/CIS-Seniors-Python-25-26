'''
File: Fitness tracker
Name: Xaiden Morey
Class: CIS Seniors
Date: 9/23/2025
'''

# Cellecting Data
name = input("Please enter your name: ")
age = int(input("Please Enter your age: "))
weight = float(input("Please Enter your weight: "))
height = int(input("Please enter your height in inches: "))
hoursExcersized = float(input("How many hours a week do your excersize? "))
fitnessGoal = input("What is your fitness goal? ")

# Computations

bmi = (weight / (height ** 2)) * 703
minutesExcersized = (hoursExcersized * 60) / 7
calsWeekly = hoursExcersized * 300

# Print Data
print("\n\n\n")
print("Personal Information:")
print("name: " + name)
print("age: ", age)
print("weight: ", weight)
print("Height: ", height)

print("\n\n\n")
print("Fitness Metrics:")
print("Your bmi is ", bmi)
print("You excersize ", hoursExcersized, " hours weekly.")
print("You need ", minutesExcersized, " minutes per week")
print("You need " , calsWeekly, " calories per week.")

print("Goal: " + fitnessGoal)
