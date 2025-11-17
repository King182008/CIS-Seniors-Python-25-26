def display_welcome():
    """Display welcome banner"""
    name = input("What is your name? ")
    print("Hello " + name + "! Welcome to your personalized college application tracker.")

def get_college_count():
    "Get the number of colleges they want to apply to and return the count as an int"
    count = int(input("How many colleges would you like to apply to? "))
    return count

def get_application_cost(count):
    total_cost = count * 25.00

    return total_cost

def get_sat_score():
    sat_score = int(input("What was your SAT score? "))

    return sat_score

def analyze_sat(score):
    if score >= 1400:
        feedback = ("SAT is Excellent")
    elif 1200 <= score < 1400:
        feedback = ("SAT is Great")
    elif 1000 <= score < 1200:
        feedback = ("SAT is Good")
    else:
        feedback = ("SAT is Terrible")

    return feedback

def display_summary(num, cost, score, feedback):
    print("\nSummary")
    print("\nNumber of Colleges: " + str(num))
    print("Cost of Applictaions: $" + str(cost))
    print("SAT Score: " + str(score))
    print("SAT Feedback: " + feedback)



def main():
    '''Main Function - orchestrates the entire program'''
    # Welcome the user
    display_welcome()

    # collect information
    num_colleges = get_college_count()
    total_cost = get_application_cost(num_colleges)
    sat = get_sat_score()

    # Analyze data
    feedback = analyze_sat(sat)

    #display results
    display_summary(num_colleges, total_cost, sat, feedback)

    print("\nGood luck with your applications")


# entry point
if __name__ == "__main__":
    main()