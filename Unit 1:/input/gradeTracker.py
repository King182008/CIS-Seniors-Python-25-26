''''
File: Grade Tracker
Name: Xaiden Morey
Class: CIS Seniors
Date: 9/26/2025
'''

print("=" * 40)
print("Welcome to your personalized grade Tracker")
print("=" * 40)

studentCount = int(input("How many student's grades are you tracking? "))

studentNameList = []
studentScoreList = []
studentLetterScore = []
passing = []
average = []
letterGrade = []
gradeDistribution = {}
totalScore = 0
totalPassed = 0

# Get inputs
for count in range(1, studentCount + 1):
    studentName = input("What is student " + str(count) + "'s name? ")
    studentNameList.append(studentName)
    studentScore = int(input("What is the student " + str(count) + "'s score? (0 - 100) "))
    studentScoreList.append(studentScore)

# Calculations
totalScore = sum(studentScoreList)
averageScore = totalScore / studentCount

for count in range(1, studentCount + 1):
    if studentScoreList[count - 1] > 70:
        totalPassed += 1

# zip lists together, sort and unzip
# .zip() - is a function that can put lists together and pair data creating a grouped element
students = list(zip(studentNameList, studentScoreList))
students.sort(key=lambda x: x[1], reverse=True)
studentNameList, studentScoreList = zip(*students)

for count in range(1, studentCount + 1):
    if 90 <= studentScoreList[count - 1] <= 100:
        letterScore = "A"
        studentLetterScore.append(letterScore)
        isPassing = "True"
        passing.append(isPassing)
        letterGrade.append(letterScore)
    elif 80 <= studentScoreList[count - 1] < 90:
        letterScore = "B"
        studentLetterScore.append(letterScore)
        isPassing = "True"
        passing.append(isPassing)
        letterGrade.append(letterScore)
    elif 70 <= studentScoreList[count - 1] < 80:
        letterScore = "C"
        studentLetterScore.append(letterScore)
        isPassing = "True"
        passing.append(isPassing)
        letterGrade.append(letterScore)
    else:
        letterScore = "F"
        studentLetterScore.append(letterScore)
        isPassing = "False"
        passing.append(isPassing)
        letterGrade.append(letterScore)

for grade in letterGrade:
    if grade in gradeDistribution:
        gradeDistribution[grade] += 1
    else:
        gradeDistribution[grade] = 1

for count in range(1, studentCount + 1):
    if studentScoreList[count - 1] > averageScore:
        aboveAverage = "True"
        average.append(aboveAverage)
    else:
        aboveAverage = "False"
        average.append(aboveAverage)

# Format and Display 
print("=" * 40)
print("%14s%7s%14s%9s%15s" % ("Student's Name", "Grade", "Letter Grade", "Passing", "Above Average"))

for count in range(1, studentCount + 1):
    print("%14s%7d%14s%9s%15s" % (studentNameList[count - 1], studentScoreList[count - 1], studentLetterScore[count - 1], passing[count - 1], average[count - 1]))

print("=" * 40)
print("\t\tSummary")
print("=" * 40)
print("Total Points: " + str(totalScore))
print("Average Class Score: " + str(averageScore))
print("Highest Score: " + studentNameList[0] + ", " + str(studentScoreList[0]))
print("Lowest Score: " + studentNameList[studentCount - 1] + ", " + str(studentScoreList[studentCount - 1]))
print("Toatal Passed: " + str(totalPassed))
print("=" * 40)
print("\tGrade Distribution")
print("=" * 40)

# .items() - get all the key value pairs
# sorted() - sorts them in alpabetical ordor
# for grade, count in - assigns the key value pairs to grade and count variables
# print(f"{grade}: {count}") - f string, acts as a quick way to add variables to a string
for grade, count in sorted(gradeDistribution.items()):
    print(f"{grade}: {count}")