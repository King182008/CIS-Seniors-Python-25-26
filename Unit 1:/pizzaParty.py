'''
File: Pizza Party
Name: Xaiden Morey
Date: 10/16/2025
Class: CIS Seniors

Program Specifications. Write a program to calculate the cost of hosting three pizza parties on Friday, Saturday and Sunday. Read from input the number of people attending, the average number of slices per person and the cost of one pizza. Dollar values are output with two decimals. For example, print(f"Cost: ${cost:.2f}").
'''
import math
SLICES = 8
TAX_RATE = 0.07
DELIVERY = 0.2

weekend_cost = 0

# Inputs
print("Enter the number of people, average slices per person, and pizza cost with a spae between each, Ex. 4 2 18")
num_people, average_slices, pizza_cost = input().split()

num_people = int(num_people)
average_slices = float(average_slices)
pizza_cost = float(pizza_cost)

# Calculate Cost
pizzas = (average_slices * num_people) / SLICES
num_pizzas = math.ceil(pizzas)
cost = num_pizzas * pizza_cost
tax = cost * TAX_RATE
deliver_fee = (cost + tax) * DELIVERY
total_cost = cost + tax + deliver_fee
weekend_cost += total_cost

# Output the bill summary
print("\nFriday Night party")
print(f"{num_pizzas} Pizzas: ${cost:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Delivery: ${deliver_fee:.2f}")
print(f"Total Cost: ${total_cost:.2f}")

# Input Saturday
print("\n")
print("Enter the number of people, average slices per person, and pizza cost with a spae between each, Ex. 4 2 18")
num_people, average_slices, pizza_cost = input().split()

num_people = int(num_people)
average_slices = float(average_slices)
pizza_cost = float(pizza_cost)

# Calculate Cost
pizzas = (average_slices * num_people) / SLICES
num_pizzas = math.ceil(pizzas)
cost = num_pizzas * pizza_cost
tax = cost * TAX_RATE
deliver_fee = (cost + tax) * DELIVERY
total_cost = cost + tax + deliver_fee
weekend_cost += total_cost

#Output bill
print("\nFriday Night party")
print(f"{num_pizzas} Pizzas: ${cost:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Delivery: ${deliver_fee:.2f}")
print(f"Total Cost: ${total_cost:.2f}")

# Input Sunday
print("\n")
print("Enter the number of people, average slices per person, and pizza cost with a spae between each, Ex. 4 2 18")
num_people, average_slices, pizza_cost = input().split()

num_people = int(num_people)
average_slices = float(average_slices)
pizza_cost = float(pizza_cost)

# Calculate Cost
pizzas = (average_slices * num_people) / SLICES
num_pizzas = math.ceil(pizzas)
cost = num_pizzas * pizza_cost
tax = cost * TAX_RATE
deliver_fee = (cost + tax) * DELIVERY
total_cost = cost + tax + deliver_fee
weekend_cost += total_cost

#Output bill
print("\nFriday Night party")
print(f"{num_pizzas} Pizzas: ${cost:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Delivery: ${deliver_fee:.2f}")
print(f"Total Cost: ${total_cost:.2f}")

# Print the Weekend Total
print("\n")
print(f"The total income from the weekend is: ${weekend_cost:.2f}")