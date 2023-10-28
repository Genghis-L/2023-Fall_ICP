# Copyright 2023 Genghis, 骆可瀚, kl4747@nyu.edu

# make the turtle graphics module available
import turtle

# also make the random module available
import random

# set up our graphical canvas
# width = 500, height = 500
turtle.setup(500, 500)

# hide the turtle
turtle.hideturtle()

# set the speed to the absolute fastest speed possible
turtle.speed(0)

# loop 100 times
for j in range(100):

    # pick up the pen and move to a random position on the screen
    turtle.penup()
    turtle.goto(random.randint(-250, 250), random.randint(-250, 250))
    turtle.pendown()

    # draw a square here
    for side in range(4):
        turtle.forward(100)
        turtle.right(90)
