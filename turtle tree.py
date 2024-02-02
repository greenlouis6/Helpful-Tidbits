bl = 100
import turtle
t = turtle.Pen()
t.speed(2)
turtle.bgcolor(input("what would you like the background to be? no red, orange or yellow please."))
t.left(90)
def branchsplit (bl):
    c = bl
    bl = c * 0.75
    t.right(45)
    t.forward(bl)
    t.dot()
    t.backward(bl)
    t.left(90)
    t.forward(bl)
    t.dot()
    t.backward(bl)
def tree():
    t.pendown()
    t.pencolor("red")
    t.width(7)
    t.forward(bl)
    t.pencolor("orange")
    t.width(4)
    branchsplit(bl)
    t.forward(75)
    t.pencolor("yellow")
    t.width(1)
    branchsplit(bl)
    t.penup()
    t.right(180)
    from math import sqrt
    t.forward(sqrt((75 * 75) * 2))
    t.pendown()
    t.left(45)
    branchsplit(bl)
    t.penup()
    
r = int(input("How many trees do you want?"))      
for v in range(r):
    t.penup()
    import random
    x = random.randrange(-turtle.window_width()//2, turtle.window_width()//2 )
    import random
    y = random.randrange(-turtle.window_height()//2, turtle.window_height()//2)
    t.goto(x,y)
    tree()


