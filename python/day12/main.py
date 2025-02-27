# Day 12: Scope and Variable Types

# first lesson practice
# prime number checker

# def prime_number(num):
#     if num <= 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# print(prime_number(44))

# PROJECT 12: NUMBER GUESSING GAME
from random import randint

print("Welcome to the Number Guessing Game!")
print("\nI am thinking of a number between 1 and 100.")
number = randint(1, 100)

# print(number)

def guess_function(level):
    """
    Handles the guessing logic for the game.

    Parameters:
        level (int): The number of attempts the player has to guess the correct number.

    The player guesses a number, and feedback is given whether the guess is too high, too low, or correct.
    If the player runs out of attempts, the game ends with a "Game Over" message.
    """
    while level >= 1:
        print(f"\nYou've got {level} attempts to guess the number right.")
        guess = int(input("\nMake a guess: "))
        if guess == number:
            print(f"\nYou got it! The answer is {guess}")
            break
        elif guess > number:
            level -= 1
            if level > 0:
                print("\nGuess is too high..Guess again.")
        else:
            level -= 1
            if level > 0:
                print("\nGuess is too low..Guess again.")
    else:
        print(f"\nGame Over...the number is {number}")

def play_game():
    """
    Handles the overall game flow and allows the player to choose a difficulty level.

    Prompts the player to select a difficulty mode ('easy', 'medium', or 'hard') and assigns 
    the corresponding number of attempts for the guessing game.

    Calls the `guess_function` to start the guessing logic based on the chosen difficulty level.
    """
    mode = input("\nChoose a Difficulty level. Type 'easy' or 'medium' or 'hard': ").lower()
    if mode == 'easy':
        level = 10
        guess_function(level)
    if mode == 'medium':
        level = 7
        guess_function(level)
    if mode == 'hard':
        level = 5
        guess_function(level)


# Main game loop
play_game()
playing = True
while playing:
    wanna_play_again = input("\nWanna Play Again? 'yes' or 'no' ").lower()
    if wanna_play_again == 'yes':
        play_game()
    else:
        print('Goodbye. Hoping to see you again!!')
        playing = False
        quit()
