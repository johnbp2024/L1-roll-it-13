# function goes here
def yes_no(question):
    """checks user response to question is yes or no/y or n then returns yes or no then"""
    while True:
        response = input(question).lower()
        #  #user says yes/no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes or no")


def instructions():
    """prints instructions"""
    print("""
***instructions***

roll the dice and try to win
    """)


def int_cheak():

    error = "please enter a integer more or equal to 13"
    while True:
        try:
            response = int(input("what is the game goal? "))
            if response < 13:
                print(error)
            else:
                return response
        except ValueError:
            print(error)

# main routine goes here

want_instructions = yes_no("do you want to see the instructions? ").lower()
if want_instructions == "yes":
    instructions()
print()
game_goal = int_cheak()
print(game_goal)
