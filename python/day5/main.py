student_scores = [3, 7, 12, 19, 24, 31, 42, 56, 67, 89]
# highest_number = max(student_scores)
# print(highest_number)

# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(score)


# number_sum = 0
# for i in range(1,101):
#     number_sum += i
# print(number_sum)


# Project 5: RANDOM PASSWORD GENERATOR

from random import choice, randint, shuffle
from string import ascii_letters

print("Welcome to the PyPassword Generator!")
letters_count = int(input("How many letters would you like in your password? "))
symbols_count = int(input("How many symbols would you like in your password? "))
numbers_count = int(input("How many numbers would you like in your password? "))
lst = []
random_letters = ""
for _ in range(letters_count):  # Generate 10 random letters
    random_letters =  choice(ascii_letters)
    lst.append(random_letters)

symbols = "!@#$%^&*()-_+=[]{}|;:,.<>?/"
random_symbols = ""
for _ in range(symbols_count):
    random_symbols = choice(symbols)
    lst.append(random_symbols)    
    
random_numbers = ""
for _ in range(numbers_count):
    random_numbers = str(randint(0, 9))
    lst.append(random_numbers)
    

print(lst)
shuffle(lst)
print(lst)

print(f"Your password is: {lst}")
