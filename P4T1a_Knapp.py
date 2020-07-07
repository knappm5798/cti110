
# Squares with Loop
# 20200704
# CTI-110 P4T1a
# Michael Knapp

#Import turtle
import turtle

#Constants
NUM_SQUARES=100
ANIMATION_SPEED=0
side=side_unit=30

#Set Up Turtle
turtle.speed(ANIMATION_SPEED)
turtle.hideturtle()

#Loop for the square
for sq in range(NUM_SQUARES + 1):
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    side=side_unit + 3 * sq

    turtle.goto(0,0)

turtle.exitonclick()