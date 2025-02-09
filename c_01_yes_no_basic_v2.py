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


# main routine goes here

want_instructions = yes_no("do you want to see the instructions? ").lower()
want_coffee = yes_no("do you want coffee")

print("we done")
