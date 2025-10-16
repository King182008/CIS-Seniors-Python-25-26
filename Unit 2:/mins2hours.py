'''
file: Minutes to hours
name: Xaiden Morey
Date: 10/14/2025
Class: CIS Seniors

Convert a set number of minutes to hours
'''

minutes = int(input("Enter minute: "))
hours = minutes // 60
mins_remaining = minutes % 60

print(minutes, "minutes(s) is", hours, "hour(s)", mins_remaining, "minutes(s)")