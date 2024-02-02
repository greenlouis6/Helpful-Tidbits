import turtle
t = turtle.Pen()
t.speed(0)
t.penup()
t.setpos(-50,200)
t.pendown()
for x in range(40):
    t.pencolor("gold")
    t.forward(500)
    t.left(35)
    t.forward(5)
    t.left(70)
    t.left(5)
    t.left(35)
for x in range(40):
    t.pencolor("red")
    t.forward(500)
    t.left(35)
    t.forward(5)
    t.left(70)
    t.left(5)
    t.left(35)
print("Hello! I am here to help with your math homework!")
print("Just type your math homework problems each time, ask me to tell you about math functions like pi by saying 'question' or type in 'done' to finish!(Just dont use uppercase.)")
problem = input("What is the first problem?")

while problem != 'done':
    if problem != 'question':
        import random
        b = (random.randrange(1,4))
    
        if b == 1:
            print("That would be ", eval(problem), ".")

        if b == 2:
            print((problem), " is", eval(problem), ".")

        if b == 3:
            print((problem), " equals", eval(problem), ".")

        print("Ok, Let's do the next problem or just enter 'done' to finish.")

        c = random.randint(1,4)

        if c == 1:
        
            problem = input("What is the next question?")

        if c == 2:
        
            problem = input("Next!")

        if c == 3:
        
            problem = input("Keep going! Whats next?")
            
import random
d = random.randint(0,4)
if d == 1:  
    print("goodbye!")
if d == 2:    
    print("Good luck on your grades. See you next time!")
if d == 3:
    print("Good job. I'll be here when you need me again. Bye!")
if d == 4:
    more = random.randint(0,3)
    if more == 1:
        answer = input("Quick question. How was school today? (Please don't use  words like amazing or terrible, I can't understand them.")
    if more == 2:
        answer = input("Quick question. Did you like school today? (Please don't use  words like amazing or terrible, I can't understand them.")
    if more == 3:
        answer = input("Just curious, did you understand your classwork today? (Please don't use longer words like amazing or terrible, I can't understand them.")
    if answer == "good" or answer == "yes" or answer == "great" or answer == "yeah" or answer == "yep" or answer == "okay" or answer == "ok":
        print("I'm glad to hear.")
        import random
        d = random.randint(0,3)
        if d == 1:  
            print("goodbye!")
        if d == 2:    
            print("Good luck on your grades. See you next time!")
        if d == 3:
            print("Good job. I'll be here when you need me again. Bye!")
            
    if answer == "bad" or answer == "very bad" or answer == "no" or answer == "not really" or answer == "not good":
        decision = input("I'm sorry to hear that. I have a interesting skill you might have used before if you have used me. It's called 'Forest Grower'. Wanna see it?")
    if decision == "sure" or decision == "okay" or decision == "ok" or decision == "yeah" or decision == "yes" or decision == "fine":
        turtle.clear()
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
            print("Hope you feel happier now. But I have an appointment to clean my database, so best wishes till next time!")

