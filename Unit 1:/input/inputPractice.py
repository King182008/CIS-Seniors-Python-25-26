'''
File Name: inputPractice.py
Name: Xaiden Morey
Class: CIS Seniors
Date: 9/19/20225

ask:
First Name
Last Name
Favorite Color
First Number
Second Number
Favorite TV Show
Favorite Movie
Favorite Song
Favorite Food

- Write out a paragraph outlining the user data using variables. Using the first and second numbers,
create 3 saperate math equations, and print out the values from the expressions
'''

firstName = input("Enter your fisrt name: ")
lastName = input("Enter your last name: ")
favColor = input("What is your favorite color: ")
num1 = input("Please input a random number: ")
num2 = input("Please input another random number: ")
FavShow = input("Please input your favorite show: ")
favMovie = input("Please input your favorite movie:")
favSong = input("Please input your favorite song:")
favFood = input("Please input your favorite food:")

print("Hello my name is " + firstName + " " + lastName + ". My favorite color is " + favColor + " because it looks really good on everything. My favorite show is " + FavShow + " because it's really funny. My favorite movie is " + favMovie + ". I really like the plot. My favorite song is " + favSong + " because I really like the lyrics and beat. My favorite food is " + favFood + "because they're just so yummy.")

equation1 = int(num1) + int(num2)
print("Number 1 plus number 2 equals ", equation1)

equation2 = int(num1) * int(num2)
print("Number 1 times number 2 equals ", equation2)

equation3 = int(num2) / int(num1)
print("Number 2 divided by number 1 equals ", equation3)

