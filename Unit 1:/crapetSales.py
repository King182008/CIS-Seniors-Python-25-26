'''
File: Carpet Sales
name: Xaiden Morey
Date: 10/16/2025
Class: CIS Seniors
'''
# Initialize Constants
TAX_RATE = 0.07
WASTE_PCT = 1.2
LABOR_RATE = 0.75

totalSales = 0

price = float(input("What is the prie per square foot? "))
length = int(input("What is the length of the room? "))
width = int(input("What is the width of the room? "))

sq_feet = (width * length)
cost = (sq_feet * price) * WASTE_PCT

# Labor costs
laborCost = sq_feet * LABOR_RATE

# Sales sales tax (7%)
tax = (cost + laborCost) * TAX_RATE
totalCost = cost + laborCost + tax

# Output Results
print("Order #1")
print("Room:", sq_feet, "sq ft")
print(f"Carpet: ${cost:.2f}")
print(f"Labor: ${laborCost:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total Cost: ${totalCost:.2f}")
totalSales += totalCost

# Order 2

# Input
print("\nFor order 2, add the price per sq ft, width, and length all seperated by a space. Ex. 2.45 16 10")
price, width, length = input().split()

price = float(price)
width = int(width)
length = int(length)

# Calculations
sq_feet = width * length
cost = (sq_feet * price) * WASTE_PCT
laborCost = sq_feet * LABOR_RATE
tax = (cost + laborCost) * TAX_RATE
totalCost = cost + laborCost + tax

# Output 2
print("Order #2")
print("Room:", sq_feet, "sq ft")
print(f"Carpet: ${cost:.2f}")
print(f"Labor: ${laborCost:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total Cost: ${totalCost:.2f}")
totalSales += totalCost

# Order 3

# Input
print("\nFor order 3, add the price per sq ft, width, and length all seperated by a space. Ex. 2.45 16 10")
price, width, length = input().split()

price = float(price)
width = int(width)
length = int(length)

# Calculations
sq_feet = width * length
cost = (sq_feet * price) * WASTE_PCT
laborCost = sq_feet * LABOR_RATE
tax = (cost + laborCost) * TAX_RATE
totalCost = cost + laborCost + tax

# Output 3
print("Order #3")
print("Room:", sq_feet, "sq ft")
print(f"Carpet: ${cost:.2f}")
print(f"Labor: ${laborCost:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total Cost: ${totalCost:.2f}")
totalSales += totalCost

# Output Total Sales
print(f"\nTotal Sales: ${totalSales:.2f}")