'''
file: Personal Finance
name: Xaiden Morey
Date: 11/18/2025
Class: CIS Seniors

Demonstartes proper python program structure using main()
'''

def display_header():
    print("=" * 40)
    print("Welcome to your personal finance tracker")
    print("=" * 40)

def get_user_name():
    name = input("Please enter your name: ")
    return name

def get_income():
    income = input("Please enter your monthly earnings ($): ")
    income = float(income)
    return income

def get_expenses():
    print("\n--- EXPENSE TRACKING ---")

    expenses = {}

    print("Enter your rent/housing cost: $", end="")
    expenses['Rent/Housing'] = float(input())

    print("Enter your food/grocery budget: $", end="")
    expenses['Food/Grocery'] = float(input())

    print("Enter your transportation cost: $", end="")
    expenses['Transportation'] = float(input())

    print("Enter your entertainment budget: $", end="")
    expenses['Entertainment'] = float(input())

    print("Enter your savings goal: $", end="")
    expenses['Savings'] = float(input())

    print("Enter miscellaneous expenses: $", end="")
    expenses['Miscellaneous'] = float(input())

    total = sum(expenses.values())

    return expenses, total


def calculate_remaining(income, expenses):
    remaning = income - expenses
    return remaning

def provide_feedback(remaining, income):
    if remaining >= income * .8:
        feedback = "Excelant"
    elif remaining >= income * .6:
        feedback = "Great"
    elif remaining >= income * .4:
        feedback = "Good"
    elif remaining >= income * .01:
        feedback = "Ok"
    else:
        feedback = "Terrible"

    return feedback

def display_summary(name, income, expenses_dict, total_expenses, remaining, feedback):
    print("\n")
    print("=" * 50)
    print(name + "'s Summary")
    print("=" * 50 + "\n")
    print("Total Income: " + str(income))
    print("\nExpenses:")
    for key, value in expenses_dict.items():
        print(f"{key}: ${value}")
    print("Total Expenses: " + str(total_expenses))
    print("\n")
    print("Remaining: $" + str(remaining))
    print("feedback: " + feedback)

def main():
    '''Main function - coordinates the entire program. Main reads like a story'''

    display_header()
    user_name = get_user_name()
    monthly_income = get_income()
    expense_categories, total_expenses = get_expenses()
    remaining = calculate_remaining(monthly_income, total_expenses)
    feedback = provide_feedback(remaining, monthly_income)
    display_summary(user_name, monthly_income, expense_categories, total_expenses, remaining, feedback)


if __name__ == "__main__":
    main()