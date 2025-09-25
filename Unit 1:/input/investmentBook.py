'''
File: Investment
Name: Xaiden Morey
Class: CIS Seniors
Date: 9/22/2025

Compute Investment Report

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

print("\n\n")
print("=" * 100)
print("My Investment Tracker")
print("=" * 100)

# Accept the inputs
startingBalance = float(input("Enter the investment amount: "))
years = int(input("Enter the numbers of year: "))
rate = int(input("Enter the rate as a %: "))

# Convert the rate to a decimal
rate = rate / 100

# Initialize the accumulator for the interest
totalInterest = 0.0

# Display the header for the table

print("%4s%18s%10s%16s" % ("Year", "Starting balanace", "Interest", "Ending balance"))

# Compute and display the results for each year

for year in range(1, years + 1):
    interest = startingBalance * rate
    endBalance = startingBalance + interest
    print("%4d%18.2f%10.2f%16.2f" % (year, startingBalance, interest, endBalance))
    startingBalance = endBalance
    totalInterest += interest

# Display the totals for the period
print("Ending balance: $%0.2f" % endBalance)
print("Total interest earned: $%0.2f" % totalInterest)