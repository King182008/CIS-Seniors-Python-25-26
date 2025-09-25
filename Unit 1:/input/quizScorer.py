'''
File: Quiz Scorer
Name: Xaiden Morey
Class: CIS Seniors
Date: 9/25/2025
'''

# Get Inputs
name = input("What is your name? ")
questions = int(input("How many questions are on the quiz"))

studentAnswers = []
quizAnswers = []
correctAnswers = 0

print("What are the students answers? (1 for True 0 for False)")
for count in range(1, questions + 1):
    sAnswer = list(input("Question" + str(count) + ":"))
    studentAnswers.append(sAnswer)

print("=" * 40)
for count in range(1, questions + 1):
    qAnswer = list(input("Quiz Answer " + str(count) + ":"))
    quizAnswers.append(qAnswer)

print("=" * 40)
for count in range(1, questions + 1):
    if studentAnswers[count - 1] == quizAnswers[count - 1]:
        print("Question" + str(count) + ": Correct")
        correctAnswers += 1
    elif studentAnswers[count - 1] != quizAnswers[count - 1]:
        print("Question" + str(count) + ": Wrong")
    
correctAnswers = round((int(correctAnswers) / int(questions)) * 100)
print(name + " got " + str(correctAnswers) + "% / 100%")

if correctAnswers >= 70:
    print(name + " passed, Good Job!")
else:
    print(name + " failed, You Suck!")