import random


def name_validity(name):
    validity = name.isalpha()
    if not validity:
        print(f"> Your name probably contains ONLY letters.")
    if len(name) < 2:
        print(f"> Your name is probably longer than 1 letter.")
        validity = False
    if not validity:
        print("> You can try again.")
    return validity


def game_round(player_move, user):
    valid_choice = False
    valid_choices = ("r", "s", "p")
    while not valid_choice:
        if player_move == "q":
            quit()
        elif player_move not in valid_choices:
            print(f"> {user}, {player_move} is not a valid option; \n Please pick again: r or R for ROCK, p or P for Paper, s or S for Scissors and q to QUIT!")
            player_move = input("> ")
        elif player_move in valid_choices:
            valid_choice = True
    computer_move = random.choice(valid_choices)
    outcome_of_round = ""
    if player_move == "r" and computer_move == "r":
        print(f"> {user} -> 🧱 | Computer -> 🧱 - it's a DRAW!")
        outcome_of_round = "draw"
    elif player_move == "s" and computer_move == "s":
        print(f"> {user} -> ✂ | Computer -> ✂ - it's a DRAW!")
        outcome_of_round = "draw"
    elif player_move == "p" and computer_move == "p":
        print(f"> {user} -> 🧻 | Computer -> 🧻 - it's a DRAW!")
        outcome_of_round = "draw"

    elif player_move == "p" and computer_move == "r":
        print(f"> {user} -> 🧻 | Computer -> 🧱 - you WIN this round")
        outcome_of_round = "win"
    elif player_move == "r" and computer_move == "s":
        print(f"> {user} -> 🧱 | Computer -> ✂ - you WIN this round")
        outcome_of_round = "win"
    elif player_move == "s" and computer_move == "s":
        print(f"> {user} -> ✂ | Computer -> 🧻 - you WIN this round")
        outcome_of_round = "win"

    elif player_move == "p" and computer_move == "s":
        print(f"> {user} -> 🧻 | Computer -> ✂ - you LOSE this round")
        outcome_of_round = "lose"
    elif player_move == "r" and computer_move == "p":
        print(f"> {user} -> 🧱 | Computer -> 🧻 - you LOSE this round")
        outcome_of_round = "lose"
    elif player_move == "s" and computer_move == "r":
        print(f"> {user} -> ✂ | Computer -> 🧱 - you LOSE this round")
        outcome_of_round = "lose"

    return outcome_of_round
