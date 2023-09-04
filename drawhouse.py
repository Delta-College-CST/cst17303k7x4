# This program draws a house

import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
pen = turtle.Turtle()

# Draw house
pen.penup()
pen.goto(-200, -100)
pen.pendown()
pen.goto(200, -100)
pen.goto(200, 100)
pen.penup()
pen.goto(-200, -100)
pen.pendown()
pen.goto(-200, 100)
pen.goto(0, 200)
pen.goto(200, 100)

# Draw window
pen.penup()
pen.goto(-120, 30)
pen.pendown()
pen.forward(60)
pen.right(90)
pen.forward(60)
pen.right(90)
pen.forward(60)
pen.right(90)
pen.forward(60)
pen.right(90)

# Draw door
pen.penup()
pen.goto(120, -100)
pen.pendown()
pen.goto(120,40)
pen.goto(60,40)
pen.goto(60,-100)

# Move pen outside of view
pen.penup()
pen.goto(0,-300)
