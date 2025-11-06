'''
Name: Xaiden Morey
File: Class Grade Project
Date: 10/4/2025
Class: CIS Seniors
'''

# Challenge: Complete Grade Book System

# Create a list of student dictionaries
grade_book = []

student1 = {
    "name": "Emma Rodriguez",
    "id": "S12345",
    "math": 95,
    "english": 88,
    "science": 92,
    "history": 89,
    "average": 91.75
}

student2 = {
    "name": "Marcus Chen",
    "id": "S12346",
    "math": 87,
    "english": 90,
    "science": 85,
    "history": 88,
    "average": 87.50
}

student3 = {
    "name": "Sophia Patel",
    "id": "S12347",
    "math": 98,
    "english": 96,
    "science": 94,
    "history": 97,
    "average": 96.25
}

grade_book.append(student1)
grade_book.append(student2)
grade_book.append(student3)


def print_class_report(students):
    """Prints a formatted report for all students"""
    for dictionary_item in grade_book:
        for key, value in dictionary_item.items():
            print(f"{key.capitalize()}: {value}")
        print("\n")
    pass

def find_top_student(students):
    """Returns the student with the highest average"""
    top_student = students[0]  # Start with the first student
    for student in students:
        if student["average"] > top_student["average"]:
            top_student = student
    return top_student
        
    pass


def count_honor_students(students):
    """Counts students with average >= 90"""
    honor = 0
    for student in students:
        if student["average"] > 90:
            honor += 1
    return honor

    pass

# Test your functions
print_class_report(grade_book)
top_student = find_top_student(grade_book)
honor_count = count_honor_students(grade_book)

print(f"Highest Averge is {top_student["name"]}")
print(f"Total honor roll students is {honor_count}")
print("Total students is 3")