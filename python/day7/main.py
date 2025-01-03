# from random import choice

# print("""Welcome to python fruit name pyguessing Game!!
# \nYou've got 6 lives..
# Every time you don't get a letter you loose a life.\n""")

# words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango"]

# random_fruit = choice(words).lower()
# # print(random_fruit)

# print(f"This time it's a {len(random_fruit)} lettered fruit, can you guess it? \n")


# place_holder = len(random_fruit)*"_"
# print(place_holder)

# correct_letters = []

# game_over = False
# player_lives = 6

# while not game_over:
#     print(f"You've got {player_lives} lives to use now")
#     user_input = input("Pick a letter: ").lower()
#     display = ""
    
#     for letter in random_fruit:
#         if letter == user_input:
#             display += user_input
#             correct_letters.append(user_input)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"
#     print(display)
#     if "_" not in display:
#         print("Hurray!!...You got the fruit's name")
#         break
#     elif user_input not in random_fruit:
#         player_lives -= 1
#         print("you made a wrong letter choice...pick another\n")
#         if player_lives == 0:
#             print(f"You lost....The fruit's name was {random_fruit}")
#             break
