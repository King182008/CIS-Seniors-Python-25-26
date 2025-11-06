'''
Name: Xaiden Morey
Date: 10/4/2025
Class: CIS Seniors
File: Python Dictionaries

-Student ID: "512345"
-Grade level: 12
-English Grade: 88
-Science Grade: 92
-Homework Completes: True

Task:
1. Crteate a dictionary called student1 with all the information above
2. Print the entire dictionary
3. Print just Emma's email address
4. Print just Emma's math grade
'''

# Part 1: create your dictionary
student1 = {
    "name": "Emma Rodriguez",
    "student_id": "S12345",
    "grade_level": 12,
    "email": "emma.r@school.edu",
    "math_grade": 95,
    "english_grade": 88,
    "science_grade": 92,
    "homework_completed": True
}

# Print the entire dictionary
print("Compklete student record:")
print(student1)

# Print specific values
print("\nStudent email:", student1["email"])


# Part 2

# Modify Emma's homework status
student1["homework_completed"] = False

# Update her English grade
student1["english_grade"] = 91

# Add history grade
student1["history_grade"] = 89

# Add clubs information
student1["clubs"] = ["Debate Team", "Math Club"]

# print updated information
print("\nUpdated Student Record:")
print(student1)

# Part 3: Create a funtion to calculate average grade
# Python function structure: def (keyword) functionName(arguments):
def calculate_average(student): 
    # Get all the grades
    math = student1["math_grade"]
    science = student1["science_grade"]
    english = student1["english_grade"]
    history = student1["history_grade"]
    
    #calculate the average
    total = math + science + english + history
    average = total / 4

    # Return the average
    return average

# Test your function
# function call:
average = calculate_average(student1)
print(f"\n{student1['name']}'s avergage grade:{average:.2f}")


# Part 4: Using Dictionary Methods
#1. Print all keys
print("\nAll keys in the dictionary")
print(student1.keys())

#2. Print all values
print("\n All values in the dictionary")
print(student1.values())


#3. Print all key-value pairs
print("\nAll the key-value pairs:")
print(student1.items())

#4. Safely get a phone number (doesn't exist)
phone = student1.get("phone_number")
print("\nPhone number:", phone)

#5. Create new student and use update()
student2 = {
    "name": "Marcus Chen",
    "student_id": "S12346"
}

student2.update(grade_level = 11, math_grade = 87, english_grade = 90, science_grade = 85)

# Use. update() to add these feilds all at once:
# grade_level: 11, math_grade: 87, english_grade 90, science_grade: 85

print("\n")
print(student2)