import turtle
import random

#define players
die_player = [1,2,3,4,5,6]
Z1 = input('write your name and press enter :  ')
Y1 = random.choice(die_player)
print(Z1 + 'is')
print(Y1)
Z2 = input('write your name and press enter :  ')
X1 = random.choice(die_player)
print(Z2 + 'is')
print(X1)

player_1 = input('Write the name of Player 1:   ')

player_2 = input('Write the name of Player 2:   ')


player_1_colour = "player_1_colour"
player_2_colour = "player_2_colour"

player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()

x = input('delay for screen set:    ')

player_one.goto(-200,100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200,-100)


player_one.goto(300,60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200,100)
player_two.goto(300,-140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200,-100)


die_player = [1,2,3,4,5,6]


for i in range(20):
    if player_one.pos() >= (300,100):
            print( player_1 + "Player One Wins!")
            break
    elif player_two.pos() >= (300,-100):
            print( player_2 + "Player Two Wins!")
            break
    else:
            player_one_turn = int(input( player_1 + "     write number in 6 to 12:  "))
            die_outcome = random.choice(die_player)
            #die_outcome = player_one_turn - die_outcome
            print("The result of the die roll is: ")
            print(die_outcome)
            print("The number of steps will be: ")
            print(10*die_outcome)
            player_one.fd(10*die_outcome)
            
            player_two_turn = int(input(player_2 + "     write number in 6 to 12:  "))
            d = random.choice(die_player)
            #die_outcome = player_two_turn - d
            print("The result of the die roll is: ")
            print(d)
            print("The number of steps will be: ")
            print(10*d)
            player_two.fd(10*d)
