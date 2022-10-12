from stages import stages
from countries import countries

import random
import os
clear = lambda: os.system('cls')
count = False
def play(score, name):
    
    chosen_word = random.choice(countries).strip().lower()
    #print(f"Pssst, the solution is {chosen_word}")
    lives = 6

    display = []
    for blank in chosen_word:
        if blank == " ":
            display.append(" ")
        else:
            display.append("_")

    entered_letters = []
    game_over = False

    while not game_over:
        print(f"{name}'s turn. Current score: {score}")
        display_txt = ''.join(display)
        print(display_txt)
        print(stages[lives])
        guess = input("Guess a letter: ").lower()
        clear()
        if guess in entered_letters:
            print(f"You already guessed '{guess}' letter. Try again.")
        else:
            entered_letters += guess
            for n in range(len(chosen_word)):
                if chosen_word[n] == guess:
                    display[n] = guess

            if guess not in chosen_word:
                lives -= 1
                print(f"You guessed '{guess}', that's not in the word. You lose a life.")
                if lives == 0:
                    game_over = True
                    print(f"You lose. The answer was: {chosen_word}")
                    print(display_txt)
                    print(stages[lives])

            if "_" not in display:
                game_over = True
                count = True
                score += 1
                print(f"You win. The answer was: {chosen_word}")

def count_score():
    if not count:
        return 1
    else:
        return 0