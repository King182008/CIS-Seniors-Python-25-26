'''
File: Variable Name Validator
Date: 10/7/2025
Class: CIS Seniors
Name: Xaiden Morey
'''

python_keywords = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
'while', 'with', 'yield']

print("=" * 40)
print("Welcom to the Python Variabel Name Validator or PVNP for short!")
print("=" * 40)
print("Enter a python variable name and the porgram will check to see if its a valid name.")

while True:

    print("\n")
    variableNameToCheck = input("Enter your variable name or enter nothing to quit: ")
    isPythonKeyword = False

    if variableNameToCheck == "":
        break

    for count in range(1, 36):
        if variableNameToCheck == python_keywords[count - 1]:
            print("ERROR: This is a python key word which can not be used as a variable name!")
            isPythonKeyword = True
    
    firstChar = variableNameToCheck[0]

    if firstChar.isdigit() == True:
        print("ERROR: The variable name can not start with a number!") 
    if variableNameToCheck.isidentifier() == True and isPythonKeyword != True:
        print("This is a valid python variable name, Good Job!")
    elif variableNameToCheck.isidentifier() == False and firstChar.isdigit() == False:
        print("This variable name contains characters that can not be used. Only Letters, Numbers and Underscores.")