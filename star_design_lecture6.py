#impot library import

import time
import turtle

K = turtle.Turtle()
K.speed(10000)
K.getscreen().bgcolor("blue")
K.penup()
K.goto((-200,100))
K.pendown()

screen = turtle.getscreen()

# set background color of screen
screen.bgcolor("#b3daff")

# set tile of screen
screen.title("STAR AMAZING DESIGN - Karan Patel")


def star(turtle, size):
	if size <= 10:
		return
	else:
		turtle.begin_fill()
		for i in range(5):

			turtle.forward(size)
			star(turtle, size/3)
			turtle.left(216)
		turtle.end_fill()

star(K, 360)



turtle.done()
