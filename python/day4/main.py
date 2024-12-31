# day 4 lessons: randomization and 
# python uses the mersenne Twister pseudorandom number generator
# in python randomization we majorly use the random module

from random import randint, choice

print("Welcome to this python rock paper and scissors game!")
options = ["Rock", "Paper", "Scissors"]
human_choice = input("which are you picking (Rock, Paper or Scissors)? ").lower()

computer_choice = choice(options).lower()
if computer_choice == human_choice:
    print(f"You picked {human_choice}, the computer picked {computer_choice}...It's a draw!!!")
elif computer_choice == "rock" and human_choice == "paper":
    print(f"You picked {human_choice}, the computer picked {computer_choice}...Hurray You won!!")
elif computer_choice == "paper" and human_choice == "scissors":
    print(f"You picked {human_choice}, the computer picked {computer_choice}...Hurray You won!!")
elif computer_choice == "scissors" and human_choice == "rock":
    print(f"You picked {human_choice}, the computer picked {computer_choice}...Hurray You won :)!!")
else:
    print(f"You picked {human_choice}, the computer picked {computer_choice}...Sorry...You Lose ( ...")


# friends = ["Emma", "Zainab", "Liam", "Josh", "Chisom"]
# print(len(friends))
# who_pays = randint(0, len(friends)-1)
# if friends[who_pays]:
#     print(f"The person paying for today's outing is {friends[who_pays]}")