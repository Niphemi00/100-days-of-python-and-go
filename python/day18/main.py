# understanding turtle module and learning it documentation
# always look up the documentation to work with it
from turtle import Turtle, Screen
import turtle
from random import choice, randint

timmy = Turtle()
turtle.colormode(255)      
screen = Screen()



def randomcolor():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)  
    random_color = (r, g, b)
    return random_color

colorChoice =  ["dark blue", 'orchid', "violet", 'thistle', "dark salmon", 'Pale Turquoise', 'magenta3', "bisque", "khaki", "LawnGreen", "DarkOrchid4"]



# SQUARE
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

#ROAD DASHED LINES
# for numbers in range(50):
#     if (numbers in range(0,10)) or (numbers in range(20,30)) or (numbers in range(40,50)):
#         timmy.forward(10)
#         timmy.penup()
#         timmy.forward(10)
#         timmy.pendown()
#     elif (numbers in range(11,20)) or (numbers in range(30,40)):
#         timmy.penup()

# DRAW POLYGONS
# for i in range(2, 10):
#     timmy.color(choice(colorChoice))
#     for _ in range(i):
#         timmy.forward(100)
#         timmy.left(360/i)


# RANDOM WALK
# direction = [0, 90, 180, 270]
# length = [10, 30, 50, 70, 100]

# for _ in range(200):
#     timmy.width(3)
#     timmy.color(randomcolor())
#     timmy.forward(choice(length))
#     timmy.setheading(choice(direction))
#     timmy.speed("fastest")

# SPIROGRAPH
for angle in range(0, 360, 5): 
    timmy.color(randomcolor()) 
    timmy.speed("fastest")
    timmy.setheading(angle)
    timmy.circle(100)

#SPIRAL
# timmy.left(90)
# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         timmy.color(c)
#         timmy.forward(steps)
#         timmy.right(30)

screen.exitonclick()