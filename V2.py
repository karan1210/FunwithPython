import turtle
import math
import random

K = turtle.Turtle()
turtle.colormode(255)
K.speed(100000)

for i in range(3000):
	K.forward(10)
	K.left(math.sin(i/10)*25)
	K.left(20)

turtle.done()
