# # PROJECT 20
# # SNAKE GAME
# # MODULES NEEDED: Screen, Turtle, random, time


# STEPS IN MAKING THIS PROJECT
    # Step 1: make the turtle body and food, and set up the screen
    # Step 2: set up the snake navigation system
    # step 3: set up collision of the snake (turrle) and food random positioning
    # step 4: set up the score board
    # step 5: make the snake detect collision against walls and biting it self as errors which leads to game over


import turtle
import random
import time

# Screen setup
screen = turtle.Screen()
user_choice = screen.textinput(title="Username", prompt="What's your name? ")
screen.title("DAY 20: Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# make snake
snake = turtle.Turtle()
snake.shapesize(stretch_wid=1, stretch_len=2)
snake.shape("square")
snake.color("green")
snake.penup()


# make food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-280, 280), random.randint(-280, 280))  # Random initial position

# display score
score = 0
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"{user_choice} Score: {score}", align="center", font=("Arial", 20, "normal"))

# Snake Body List for adding up in lpength
snake_body = []

# Movement Functions
def move():
    global score

    # Move the body segments (back to front)
    for i in range(len(snake_body) - 1, 0, -1):
        x = snake_body[i - 1].xcor()
        y = snake_body[i - 1].ycor()
        snake_body[i].goto(x, y)

    # Move the first segment to the snake's old position
    if len(snake_body) > 0:
        x = snake.xcor()
        y = snake.ycor()
        snake_body[0].goto(x, y)
    snake.forward(20)

    # Check Collision with Food
    if snake.distance(food) < 15:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))  # Move food
        score += 1  # Increase score
        update_score()
        grow_snake()  # Add a new segment to the snake

    # ollisions with walls or if snake bites itself
    check_game_over()

    # Keep moving
    screen.update()
    screen.ontimer(move, 150)

# Snake Direction Controls
def go_up():
    if snake.heading() != 270:  # Prevent moving backward
        snake.setheading(90)

def go_down():
    if snake.heading() != 90:
        snake.setheading(270)

def go_left():
    if snake.heading() != 0:
        snake.setheading(180)

def go_right():
    if snake.heading() != 180:
        snake.setheading(0)

# Update Score
def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Arial", 20, "normal"))

# **Fix: Properly grow the snake behind the last segment**
def grow_snake():
    new_segment = turtle.Turtle()
    new_segment.shape("square")
    new_segment.color("green")
    new_segment.penup()
    
    # Place the new segment at the last segment's position
    if len(snake_body) > 0:
        last_segment = snake_body[-1]
        new_segment.goto(last_segment.xcor(), last_segment.ycor())
    else:
        new_segment.goto(snake.xcor(), snake.ycor())

    snake_body.append(new_segment)

# Check for Game Over Conditions
def check_game_over():
    # Check if snake hits the wall
    if abs(snake.xcor()) > 290 or abs(snake.ycor()) > 290:
        game_over()
    
    # Check if snake collides with its own body
    for segment in snake_body[1:]:
        if snake.distance(segment) < 10:
            game_over()

# End the Game
def game_over():
    global score
    score_display.clear()
    score_display.goto(0, 0)
    score_display.write(f"Game Over! {user_choice}'s Final Score: {score}", align="center", font=("Arial", 24, "bold"))
    screen.update()
    time.sleep(2)
    screen.bye()

# keyboard directions and listenings
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# Start turtle movement
move()

screen.mainloop()
