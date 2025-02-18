import random

user_points = 0
comp_points = 0
double_user = "no"

user_one = random.randint( 1,  6)
user_two = random.randint( 1,  6)

if user_one == user_two:
    double_user = "yes"

comp_one = random.randint( 1,  6)
comp_two = random.randint( 1,  6)

user_points += user_one + user_two
comp_points += comp_one + comp_two

print("\ninitial_points")

print(f"user    - roll 1: {user_one} \t| roll 2: {user_two} \t| total: {user_points} ")
print(f"computer    - roll 1: {comp_one} \t| roll 2: {comp_two} \t| total: {comp_points} ")

if double_user == "yes":
    print("great job, if you win you will earn double points!")