
error = "please enter a integer more or equal to 13"
while True:
    try:
        game_goal = int(input("what is the game goal? "))
        if game_goal < 13:
            print(error)
        else:
            print(f"game goal: {game_goal}")
            break
    except ValueError:
        print(error)