import turtle
t = turtle.Turtle()
turtle.getscreen()
turtle.bgcolor("black")
t.color("White", "red")
q = "y"
while (q == "y"):
    u = input("What should I draw?\n")

    if u == "circle":
        n = float(input("Please Specify the radius\n"))

        t.circle(n)

    elif u == "square":
        n = float(input("Please Specify side size\n"))

        for i in range(4):
            t.fd(n)
            t.rt(90)
            
            
    else:
        n = float(input("Pleae Specify Diagonal"))
        t.fd(n)


    q = input("y to redraw and n to exit\n")
    t.clear()
    
