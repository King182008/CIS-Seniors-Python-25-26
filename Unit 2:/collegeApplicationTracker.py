'''
File: College Application Tracker
name: Xaiden Morey
Date: 10/24/2025
Class: CIS Seniors
'''

# Into
import math

studentName = input("What is your name? ")

print("=" * 50)
print("Welcome To Your College Application Tracker!")
print("=" * 50)

print("Welcome " + studentName + " to your college application tracker")



# Initilize Constants and lists
APPLICATION_FEE = 75.00
AVG_ACCEPTANCE_RATE = 55.0
MAX_IDEAL_DISTANCE = 500
classificationList = []
highestPrice = 0
lowestPrice = 100000000


# Collect Data in tuples
from collections import namedtuple

school = namedtuple("school", ["collegeName", "location", "annualTuition", "distanceFromHome", "acceptanceRate"])

school1 = school(input("College Name "), input("Location (city, state) "), float(input("Annual Tuition ($) ")), float(input("Distance From Home (In Miles) ")), int(input("Acceptance Rate (%) ")))
print("\n")
school2 = school(input("College Name "), input("Location (city, state) "), float(input("Annual Tuition ($) ")), float(input("Distance From Home (In Miles) ")), int(input("Acceptance Rate (%) ")))
print("\n")
school3 = school(input("College Name "), input("Location (city, state) "), float(input("Annual Tuition ($) ")), float(input("Distance From Home (In Miles) ")), int(input("Acceptance Rate (%) ")))
college = [school1, school2, school3]

# Calcualtions
applicationCost = 3 * APPLICATION_FEE
averageTuition = math.ceil(school1[2] + school2[2] + school3[2])
averageDistance = math.ceil(school1[3] + school2[3] + school3[3])

for school in college:
    if school.acceptanceRate > 50:
        classificationList.append("Safty")
    elif school.acceptanceRate > 20:
        classificationList.append("Match")
    else:
        classificationList.append("Reach")

for school in college:
    if school.annualTuition > highestPrice:
        highestPrice = school.annualTuition
    elif school.annualTuition < lowestPrice:
        lowestPrice = school.annualTuition

differenceOfPrice = highestPrice - lowestPrice


# Format and Output
print("\n--College 1--")
print(f"College Name: {school1[0]}")
print(f"Location: {school1[1]}")
print(f"Annual Tuition: ${school1[2]:.2f}")
print(f"Distance From Home: {school1[3]:.2f} Miles")
print(f"Acceptance Rate: {school1[4]}%")
print(f"Classification: {classificationList[0]}")
print(f"4 Year Total Cost: {school1[2] * 4}")

print("\n--College 2--")
print(f"College Name: {school2[0]}")
print(f"Location: {school2[1]}")
print(f"Annual Tuition: ${school2[2]:.2f}")
print(f"Distance From Home: {school2[3]:.2f} Miles")
print(f"Acceptance Rate: {school2[4]}%")
print(f"Classification: {classificationList[1]}")
print(f"4 Year Total Cost: {school2[2] * 4}")

print("\n--College 3--")
print(f"College Name: {school3[0]}")
print(f"Location: {school3[1]}")
print(f"Annual Tuition: ${school3[2]:.2f} ")
print(f"Distance From Home: {school3[3]:.2f} Miles")
print(f"Acceptance Rate: {school3[4]}%")
print(f"Classification: {classificationList[2]}")
print(f"4 Year Total Cost: {school3[2] * 4}")

print("\n")
print("=" * 50)
print("Financial Analysis")
print("=" * 50)
print(f"Total Application Fees: ${APPLICATION_FEE * 3:.2f}")
print(f"Average Annual Tuition: ${averageTuition:.2f}")
print(f"Total 4-Year Tuition (All Schools): ${averageTuition * 4:.2f}")
print(f"Most Affordable: ${averageTuition:.2f}")
print(f"Highest Price: ${highestPrice:.2f}")
print(f"Lowest Price: ${lowestPrice:.2f}")
print(f"Differance In Price: ${differenceOfPrice:.2f}")