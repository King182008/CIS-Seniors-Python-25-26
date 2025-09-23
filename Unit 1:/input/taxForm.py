'''
File: Tax Form
Name: Xaiden Morey
Class: CIS Seniors
Date: 9/22/2025

Compute a person's income tax.
1. Significant constants
    tax rate
    standared deduction
    deduction per dependent

2. The inputs are 
    gross income 
    number of dependents 

3. Computations:
    taxable income = gross income - the standared deduction - a deduction for each depednent

    income tax = is a fixed percentage of the taxable income

4. The outputs are:
    the income tax
'''
print("\n\nMy Tax Rate Calculator.")
print("=" * 40)
# Initialize the constants

TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

# Request inputs
grossIncome = float(input("Enter the gross income:"))
numDependents = int(input("How many dependents do you have: "))

# Compute the income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - \
                DEPENDENT_DEDUCTION * numDependents
incomeTax = taxableIncome * TAX_RATE

# Display the income tax
print("The income tax is $" + str(incomeTax) + "\n\n")