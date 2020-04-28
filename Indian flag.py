#python script video 5 Karan patel
#import library

import turtle
import time

# create a screen
screen = turtle.getscreen()

# set background color of screen
screen.bgcolor("#b3daff")

# set tile of screen
screen.title("Indian Flag - Karan Patel")

K = turtle.Turtle()

# set the cursor/turtle speed. Higher value, faster is the turtle
K.speed(100)
K.penup()

# decide the shape of cursor/turtle
K.shape("turtle")

# flag height to width ratio is 2:3
flag_height = 300
flag_width = 450

# starting points
# start from the first quardant, half of flag width and half of flag height
start_x = -225
start_y = 150

# For saffron, white and green stripes. each strip width will be flag_height/3 = 100
stripe_height = flag_height/3
stripe_width = flag_width

# Radius of Ashok Chakra, half of white stripe 
chakra_radius = stripe_height / 2

# Create the Rectangle
def frame_of_flage(x, y, height, width, color):
    K.goto(x,y)
    K.pendown()
    K.color(color)
    K.begin_fill()
    K.forward(width)
    K.right(90)
    K.forward(height)
    K.right(90)
    K.forward(width)
    K.right(90)
    K.forward(height)
    K.right(90)
    K.end_fill()
    K.penup()


# this function is used to create 3 stripes
def draw_stripes():
    x = start_x
    y = start_y
    
    # we need to draw total 3 stripes, 1 saffron, 1 white and 1 green
    frame_of_flage(x, y, stripe_height, stripe_width, "#FF9933")
    # decrease value of y by stripe_height
    y = y - stripe_height   
    # create middle white stripe
    frame_of_flage(x, y, stripe_height, stripe_width, "white")
    y = y - stripe_height               

    # create last green stripe
    frame_of_flage(x, y, stripe_height, stripe_width, '#138808')
    y = y - stripe_height


def draw_chakra():
    K.speed(1)
    K.goto(0,0)
    color = "#000080" # navy blue
    K.penup()
    K.color(color)
    K.fillcolor(color)
    K.goto(0, 0 - chakra_radius)
    K.pendown()
    K.circle(chakra_radius)
    # draw 24 spikes in chakra
    for _ in range(24):
        K.penup()
        K.goto(0,0)
        K.left(15)
        K.pendown()
        K.forward(chakra_radius)
  
    

# start after 5 seconds.
time.sleep(0)

# draw 3 stripes
draw_stripes()

# draw squares to hold stars
draw_chakra()

# hide the cursor/turtle
K.hideturtle()
# keep holding the screen until closed manually
screen.mainloop()
