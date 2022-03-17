# Week 10 Learn Together

import random  # added missing import random # 1


def work_today():
    # Input if the user went to work today
    print("0: No\n1: Yes")
    work_bool = int(input("Did you go to work today?: "))
    while work_bool < 0 and work_bool > 1:
        print("Invalid input!")
        work_bool = int(input("Did you go to work today?: "))
    return work_bool


def total_time():
    # Goes through the dictionary to add the number of hours
    sum_time = 0  # assigned sum_time to 0 so function would work # 2
    for day in work_out_sched:
        sum_time += work_out_sched[day]["time"]
    return sum_time


# LISTS FILLED IN
work_out_sched = {
    "Monday":
    {
        "work out": ["legs", "abs"],
        "time": 0,
    },
    "Tuesday":
    {
        "work out": ["shoulders", "back"],
        "time": 0,
    },
    "Wednesday":
    {
        "work out": ["chest", "bicepts"],
        "time": 0
    },
    "Thurday":
    {
        "work out": ["shoulders", "back"],
        "time": 0,
    },
    "Friday":
    {
        "work out": ["legs", "abs"],
        "time": 0,
    },
    "Saturday":
    {
        "work out": ["chest", "none"],
        "time": 0,
    },
    "Sunday":
    {
        "work out": ["tricepts", "none"],
        "time": 0,
    },
}

motivating_word = ["great", "wonderfull", "stupendous", "fantastic",
                   "fabulous", "splendid", "marvelous", "superb",
                   "favorable", "satisfying", "delightful", "rewarding",
                   "fulfilling", "gainful", "fruitful", "productive"]

user_name = input("What is your name?: ")

# PROMPT THE USER
print(f"{user_name}'s Weekly Gym Planner")  # changed string to f"string" # 3

for day in work_out_sched:
    # Randomly chooses a motivating word and output
    rand_word = random.randint(0, len(motivating_word)-1)
    print(f"\nToday is {day}")
    print(f"You will have a {motivating_word[rand_word]} day!")
    work_bool = work_today()

    # BASED ON THE INPUT, OUTPUT THE DAY'S SCHEDULE
    if(day == "Sunday" or day == "Saturday"):
        print("Did you miss a day of work out?")
        # added '()' after .lower # 4
        missed_day = str(input("Enter 'y' for yes: ")).lower()
        if missed_day == "y":
            work_out1 = work_out_sched[day]["work out"][0]
            print("Today we will only work out our " + work_out1)
        else:
            print("You do not need to work out today")
            print("Take a rest day!")
    else:
        work_out1 = work_out_sched[day]["work out"][0]
        work_out2 = work_out_sched[day]["work out"][1]
        # Changed work_out1 at end of print statement to work_out2 # 5
        print("Today we will work out our " + work_out1 + " and " + work_out2)

    # Decided if we need to run today
    if (work_bool == 0):
        print("Before that we will start with a mile run on the treadmill")
    elif(work_bool == 1):
        print("Today you do not need to run the mile")

    # stores the value for the num of hours in that day
    daily_time = int(input("How many hours did you work out today?: "))
    work_out_sched[day]["time"] = daily_time  # removed extra = # 6

    # prompts the user if they want to continue
    print("Will you continue working out for the week?")
    choice = input("Enter 'y' for yes: ").lower()  # add . between lower() # 7
    if not choice == 'y' or day == "Sunday":  # added : to end of line # 8
        # added '()' after total_time # 9
        print(f"\nYou worked out a total of {total_time()} hours")
        print("Hope you had a great work out!")
        print("Till next week!")
        break
