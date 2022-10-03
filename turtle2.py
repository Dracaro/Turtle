import turtle
import random

player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200, 100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200,-100)

player_one.goto(300, 100)
player_one.pendown()
player_one.rt(90)
player_one.fd(500)
player_one.backward(1000)
player_one.penup()
player_one.goto(-200, 100)
player_one.lt(90)
player_one.pendown()
player_two.pendown()
i = 1
die = [1, 2, 3, 4, 5, 6]

for i in range(20):
    if player_one.pos() >= (300, 100):
        print("Player One Wins")
        player_one.penup()
        player_one.home()
        player_one.pendown()
        while i <= 5:
            player_one.fd(0,200)
            player_one.fd(0, -200)
            i = i+1

    elif player_two.pos() >= (300,-100):
        print("Player Two Wins")
        player_one.penup()
        player_two.home()
        player_two.pendown()
        while i <= 5:
            player_two.fd(0,200)
            player_two.fd(0, -200)
            i = i +1

    
    else:
        player_one_turn = input("Press Enter To ROll the Die")

        do = int(random.choice(die))
        print("The result of the die is:")
        print(do)
        print("The number of steps will be:")
        print(do*20)
        player_one.fd(do*20)

        player_two_turn = input("Press Enter to Roll the Die")
        do = int(random.choice(die))
        print("The result of the die is: ")
        print(do)
        print("The number of steps will be:")
        print(do*20)
        player_two.fd(do*20)



