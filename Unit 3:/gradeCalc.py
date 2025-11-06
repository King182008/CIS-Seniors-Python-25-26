'''
Name: Xaiden Morey
Class: CIS Seniors
Date: 10/6/2025
File: Grade Claculator
'''

exam1_grade = float(input("Enter score on Exam 1 (out of 100): "))
exam2_grade = float(input("Enter score on Exam 2 (out of 100): "))
exam3_grade = float(input("Enter score on Exam 3 (out of 100): "))

examAvg = (exam1_grade + exam2_grade + exam3_grade) / 3

print(f"Your exam grade is: {examAvg}")

print("\n\nStudent Versions")

#1. Calculates the overall grade for four equally weighted programming assignments, in which each assignment is graded out of 50 points. Hint: First calculate the percentage for each assignment (e.g., score / 50), then calculate the overall grade percentage (be sure to multiply the result by 100).
def calculate_grade(points):
    total_points = int(input("Please enter the total number of points for this assignment: "))
    grade = points / total_points
    return grade

program1 = int(input("Enter number of points on Program 1: "))
program2 = int(input("Enter number of points on Program 2: "))
program3 = int(input("Enter number of points on Program 3: "))
program4 = int(input("Enter number of points on Program 4: "))

# Calculate each grade percentage (score/50)
grade1 = calculate_grade(program1) # Call function plus and pass aurguments
grade2 = calculate_grade(program2)
grade3 = calculate_grade(program3)
grade4 = calculate_grade(program4)


# Calculate the overall percentage
progAvg = ((grade1 + grade2 + grade3 + grade4) / 4) * 100
print(f"\nStudent program average on programming assignments {progAvg:.2f}")




#2.Calculates the overall grade for four equally weighted programming assignments, in which assignments 1 and 2 are graded out of 50 points and assignments 3 and 4 are graded out of 75 points.
assign1 = int(input("Enter the number of points for assignment 1: "))
assign2 = int(input("Enter the number of points for assignment 2: "))
assign3 = int(input("Enter the number of points for assignment 3: "))
assign4 = int(input("Enter the number of points for assignment 4: "))

assignGrade1 = calculate_grade(assign1)
assignGrade2 = calculate_grade(assign2)
assignGrade3 = calculate_grade(assign3)
assignGrade4 = calculate_grade(assign4)

assignAvg = ((assignGrade1 + assignGrade2 + assignGrade3 + assignGrade4) / 4) * 100
print(f"\nStudent assignment average on programming assignments {assignAvg:.2f}")


#3. Calculates the overall grade for a course with three equally weighted exams (graded out of 100 points) that account for 60% of the overall grade and four equally weighted programming assignments (graded out of 50 points) that account for 40% of the overall grade. Hint: The overall grade can be calculated as 0.6 * averageExamScore + 0.4 * averageProgScore.
print("\n\nSection 3 of the assignment:\n")

overallAvg = (examAvg * 0.5) + (progAvg * 0.4) + (assignAvg * 0.1)

print(f"Your exam average is: {examAvg:.2f}")
print(f"Student program average {progAvg:.2f}")
print(f"Student assignment average {assignAvg:.2f}")
print(f"The students overall average is: {overallAvg:.2f}")