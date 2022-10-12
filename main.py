import os
clear = lambda: os.system('cls')

from stages import logo
from game import play, count_score

print(logo)
print("Welcome to game 'Hangman'.")
users = int(input("Enter number of players: "))
game_over = False

users_names = []
for n in range(users):
    player = input(f"Enter name of user {n+1}: ")
    player_data = [player, 0]
    users_names += [player_data]
while not game_over:
    for user in range(users):
        player_score = 0
        play(users_names[user][1], users_names[user][0])
        users_names[user][1] += count_score()
    end_game = input("To end the game and check score press 'y', to continue press any key: ").lower()

    if end_game == "y":
        game_over = True

clear()
print("Game's over. Final score is: ")
for player, score in users_names:
    print(f"{player} : {score}")
print("The winner is: ")
winner = max(users_names)
print(f"{winner[0]}, with a score : {winner[1]}")

    
    

    
    
