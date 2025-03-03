import random

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



def initial_points(which_player):
    double = "no"

    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_two
    print(f"{which_player}    - roll 1: {roll_one} \t| roll 2: {roll_two} \t| total: {total} ")
    return total, double


def make_statement(statement, decoration):
    """adds emoji/ additional characters to the start and end of sentences"""

    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")

#main starts here
comp_score = 0
user_score = 0
rounds_played = 0

game_history = []

make_statement("welcome to the roll it 13 game!",  "🍀")

want_instructions = yes_no("do you want to see the instructions? ").lower()
if want_instructions == "yes":
    instructions()
print()
game_goal = int_cheak()

while comp_score < game_goal and user_score < game_goal:
    rounds_played += 1

    make_statement(f"round {rounds_played}", "🎲")

    initial_user = initial_points("user")
    initial_comp = initial_points("comp")

    user_points = initial_user[0]
    comp_points = initial_comp[0]

    double_user = initial_user[1]
    if double_user == "yes":
        print("great job, if you win you will earn double points!")

    first = "user"
    second = "computer"
    player_1_points = user_points
    player_2_points = comp_points

    if user_points < comp_points:
        print("you start because your initial roll was less than the computer\n")

    elif user_points == comp_points:
        print("the initial rolls where the same, the user starts!")

    else:
        player_1_points, player_2_points = player_2_points, player_1_points
        first, second = second, first

    while player_1_points < 13 and player_2_points < 13:
        print()
        input("please press enter to continue this round")
        print()

        player_1_roll = random.randint(1, 6)
        player_1_points += player_1_roll

        print(f"{first}: rolled a {player_1_roll} - has {player_1_points}points")

        if player_1_points >= 13:
            break

        player_2_roll = random.randint(1, 6)
        player_2_points += player_2_roll

        print(f"{second}: rolled a {player_2_roll} - has {player_2_points}points")

        print(f"{first}: {player_1_points}  | {second} {player_2_points}")
    # end of round
    user_points = player_1_points
    comp_points = player_2_points

    if first == "computer":
        user_points, comp_points = comp_points, user_points

    if user_points > comp_points:
        winner = "user"
        loser = "computer"
        comp_points = 0
    else:
        winner = "computer"
        loser = "user"
        user_points = 0

    round_feedback = f"the {winner} won. the {loser}'s points have been reset to zero"

    if winner == "user" and double_user == "yes":
        user_points = user_points * 2

    make_statement("round results", "=")
    print(f"user points: {user_points} | computer points: {comp_points}")
    print(round_feedback)
    print()

    comp_score += comp_points
    user_score += user_points

    game_results = f"Round {rounds_played}: user points {user_points}  |" \
                   f"computer points {comp_points},{winner} wins " \
                   f"({user_score} | {comp_score})"

    game_history.append(game_results)

    print("*** game update ***")
    print(f"User score: {user_score}  | computer score: {comp_score}")

make_statement("game over",  "🏁")

print()
if user_score > comp_score:
    make_statement("the user won" , "👍")
else:
    make_statement("the computer won", "💻" )

make_statement("game history", "🎲")

for item in game_history:
    print(item)