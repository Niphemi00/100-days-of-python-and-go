from turtle import Turtle, Screen
from random import choice

screen = Screen()
josh = Turtle()
maine = Turtle()
ishow = Turtle()
gana = Turtle()

speed_list = ['fastest', 'fast', 'normal', 'slow']

gana.shape('turtle')
josh.shape('turtle')
maine.shape('turtle')
ishow.shape('turtle')

screen.setup(width=500, height=600)
user_choice = screen.textinput(title="place your bets", prompt="Pick your winner: ")


if user_choice == "ishow":
    pass
elif user_choice == "gana":
    pass
elif user_choice == "josh":
    pass
elif user_choice == "maine":
    pass
else:
    print('Wrong Pick')


josh.color("blueviolet")
maine.color("green")
gana.color("red")

josh.penup()
josh.goto(x=-250, y=0)



gana.penup()
gana.goto(x=-250, y=50)

ishow.penup()
ishow.goto(x=-250, y=100)

maine.penup()
maine.goto(x=-250, y=-50)





screen.setup(width=500, height=700)

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