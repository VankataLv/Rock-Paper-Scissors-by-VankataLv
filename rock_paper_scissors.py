import functions
print("> Dear player, welcome to my Rock-Paper-Scissors game!")

while True:
    user_name = input("> What is your name? \n> ")
    valid_name = functions.name_validity(user_name)             # to check if the name is real
    if valid_name:
        break

user_name = user_name.capitalize()
print(f"> Hello {user_name}!\n> Let's play a game of 3 rounds!")
user_wins = 0
computer_wins = 0
draws = 0
for round_count in range(1, 4):
    print(f"> {user_name} please pick: r for ROCK, p for Paper, s for Scissors and q to QUIT!")
    result = functions.game_round(input("> "), user_name)

    if result == "win":
        user_wins += 1
    elif result == "lose":
        computer_wins += 1
    elif result == "draw":
        draws += 1

print(f"> Nice game! {user_name} has {user_wins} wins.\n> Computer has {computer_wins} wins. \n {draws} draws in between.")
