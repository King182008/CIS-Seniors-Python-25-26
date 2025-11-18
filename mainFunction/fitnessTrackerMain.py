# UNSTRUCTURED PROGRAM - Needs fixing!
# print("Fitness Tracker")
# print("===============")

# exercise = input("What exercise did you do? ")
# duration_str = input("How many minutes? ")
# duration = int(duration_str)

# calories_per_minute = 8  # Average
# total_calories = duration * calories_per_minute

# print("Exercise: " + exercise)
# print("Duration: " + str(duration) + " minutes")
# print("Calories burned: " + str(total_calories))

# if total_calories >= 240:
#         feedback = "Great workout!"
#     else:
#         feedback = "Good start! Try for 30+ minutes next time."


def display_bannar():
    print("Fitness Tracker")
    print("===============")

def user_exercise():
    exercise = input("What exercise did you do? ")
    duration_str = input("How many minutes? ")
    duration = int(duration_str)
    return exercise ,duration

def calories_burrned(time):
    calories_per_minute = 8  # Average
    total_calories = time * calories_per_minute
    return total_calories

def encouredgment(total_calories):
    if total_calories >= 240:
        feedback = "Great workout!"
    else:
        feedback = "Good start! Try for 30+ minutes next time."
    return feedback
    
def display_summary(exercise, time, burned_calories, feedback):
    print("Exercise: " + exercise)
    print("Duration: " + str(time) + " minutes")
    print("Calories burned: " + str(burned_calories))
    print("Feedback: " + feedback)

def main():
    display_bannar()
    exercise, time = user_exercise()
    burned_calories = calories_burrned(time)
    feedback = encouredgment(burned_calories)
    display_summary(exercise, time, burned_calories, feedback)

if __name__ == "__main__":
    main()