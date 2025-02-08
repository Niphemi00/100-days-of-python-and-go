from turtle import Turtle, Screen
from random import randint

screen = Screen()


## PYTHON TURTLE RACING GAME
screen.setup(width=500, height=600)
user_choice = screen.textinput(title="place your bets", prompt="Pick your winner: ")

all_turtles = []

turtle_colors = ["red", "blue", "green", "purple", "orange"]
y_index = [-200, -100, 0, 100, 200]
for player in range(5):
    players = Turtle(shape="turtle")
    players.penup()
    players.color(turtle_colors[player])
    players.goto(x=-250, y=y_index[player])
    all_turtles.append(players)

racing = False
if user_choice:
    racing = True
    
while racing:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            print(f'The {winning_color} turtle won this round')
            racing = False
            if winning_color == user_choice:
                print("You've Won!!!")
            else:
                print("You lose!!!")
        else:
            steps = randint(0, 30)
            turtle.forward(steps)

screen.exitonclick()


# # def moveForward():
# #     timmy.forward(20)


# # # learning listeners
# screen.listen()
# # screen.onkey(key="space", fun=moveForward)



# # BUILDING AN ETCH-A-SKETCH GAME

# def forward():
#     timmy.forward(20)
    
# def backward():
#     timmy.backward(20)
    
    
# def c_clockwise():
#     timmy.left(20)

    
    
# def clockwise():
#     timmy.right(20)

    
    
# def clearScreen():
#     timmy.clear()
#     timmy.penup()
#     timmy.home()
#     timmy.pendown()
    
    
    
# screen.onkey(forward, "w")
# screen.onkey(backward, "s")
# screen.onkey(c_clockwise, "a")
# screen.onkey(clockwise, "d")
# screen.onkey(clearScreen, "c")


# # for _ in range(5):
# #     print("W for moving forwards\nS for moving backwards\nA for moving counter-Clockwise\nD for Clockwise\nC to clear page...")
# #     move = input("Make a move: ").upper()
# #     if move == "W":
# #         pass
# #     elif move == "S":
# #         pass
# #     elif move == "A":
# #         pass
# #     elif move == "D":
# #         pass
# #     elif move == "C":
# #         pass
# #     else:
# #         print("Wrong Input.....Read the instruction and make a move!!")



# screen.exitonclick()

# # # when passing a function as parameter in another function, you don't add the the paranthesis

# # def add(a,b):
# #     return a + b

# # def cal(a, b, func):
# #     return(func(a,b))

# # result = cal(1, 2, add)

# # print(result)