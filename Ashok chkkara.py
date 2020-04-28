import turtle
import time

# create a screen
screen = turtle.getscreen()
# set background color of screen
screen.bgcolor("#b3daff")
# set tile of screen

screen.title("Ashok chakra - Karan Patel")

t = turtle.Turtle()
# set the cursor/turtle speed. Higher value, faster is the turtle
t.speed(1)
t.penup()
t.goto(0,0)
color = "#000080" # navy blue
t.penup()
t.color(color)
t.fillcolor(color)
t.goto(0, 0 - 100)
t.pendown()
t.circle(100)

# draw 24 spikes in chakra
for _ in range(24):
    t.penup()
    t.goto(0,0)
    t.left(15)
    t.pendown()
    t.forward(100)
