
# Using Turtle to write Initials
# 20200704
# CTI-110 P4T1B- Turtle Initials
# Michael Knapp
#
#Import turtle and choose astetics
import turtle
turtle.pencolor('Green')
turtle.pensize(15)
turtle.shape()
#Begin "M"
turtle.right(90)
turtle.forward(100)
turtle.back(100)
turtle.left(45)
turtle.forward(60)
turtle.left(90)
turtle.forward(60)
turtle.right(135)
turtle.forward(100)
#Move to start second initial
turtle.penup()
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.pendown()
#Begin "K"
turtle.forward(100)
turtle.back(50)
turtle.right(45)
turtle.forward(75)
turtle.back(75)
turtle.right(85)
turtle.forward(75)
turtle.exitonclick()