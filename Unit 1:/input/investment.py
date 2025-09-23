'''
File: Investment
Name: Xaiden Morey
Class: CIS Seniors
Date: 9/22/2025

Compute an Investment Report

1. The inputs are:
    Starting investment amount
    number of yaers
    Interest rate (an Int percent)

2. The report is displayed in tabular form with a header
3. Computations and outputs:
    for each year of the investment compute the interest and add it to the investment
    print a formatted row of results for that year

4. The ending investment and interest you have paid in total are also displayed
'''

# Accept the Integers
startingInvestment = int(input("What is the starting amount invested? "))
numYears = int(input("How many years has the investment grown? "))
interestRate = int(input("What is the rate of interest? "))
year = 1

# Convert the interest rate to a decimal
interestRate = interestRate / 100 + 1

# Computations
count = 0
while count < numYears:
    if count < numYears:
        totalInvest = (startingInvestment * interestRate)
        startingInvestment = round(totalInvest)
        print(startingInvestment, "\tYear: ", year)
        count += 1
        year += 1