# RosetteOrPolygonKaleidoscope
import random  # importing random
import turtle  # importing turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")   # background color = black

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "purple", "white", "pink"]
# range of colors

numbers = int(turtle.numinput("How Many No.Of Sides Do You Want ?", "Enter The No.Of Sides You Need :"))
# range of sides

shape = turtle.textinput("What Shape Do You Want ?", "Enter 'p' For Polygon And 'r' For Rosette")
# different shapes

for n in range(50):
    # Generate spirals of random sizes/colors at random locations on the screen
    t.pencolor(random.choice(colors))  # Pick a random color from colors[]
    size = random.randint(10, 40)      # Pick a random spiral size from 10 to 40
    # Generate a random (x,y) location on the screen
    x = random.randrange(0, turtle.window_width()//2)
    y = random.randrange(0, turtle.window_height()//2)
    
    if shape == 'p':
        # First Polygon
        t.penup()
        t.setpos(x, y)
        t.pendown()
        for m in range(size):
            t.forward(m*2)
            t.left(91)
        # Second Polygon
        t.penup()
        t.setpos(-x, y)
        t.pendown()
        for m in range(size):
            t.forward(m*2)
            t.left(91)
        # Third Polygon
        t.penup()
        t.setpos(-x, -y)
        t.pendown()
        for m in range(size):
            t.forward(m*2)
            t.left(91)
        # Fourth Polygon
        t.penup()
        t.setpos(x, -y)
        t.pendown()
        for m in range(size):
            t.forward(m*2)
            t.left(91)

for x in range(50):
    # Generate spirals of random sizes/colors at random locations on the screen
    t.pencolor(random.choice(colors))  # Pick a random color from colors[]
    size = random.randint(1, 7)        # Pick a random spiral size from 10 to 40
    # Generate a random (a,b) location on the screen
    a = random.randrange(0, turtle.window_width()//2)
    b = random.randrange(0, turtle.window_height()//2)

    if shape == 'r':
        # First Rosette
        t.penup()
        t.setpos(a, b)
        t.pendown()
        for l in range(size):
            t.circle(10)
            t.left(360/numbers)
        # Second Rosette
        t.penup()
        t.setpos(-a, b)
        t.pendown()
        for l in range(size):
            t.circle(10)
            t.left(360/numbers)
        # Third Rosette
        t.penup()
        t.setpos(-a, -b)
        t.pendown()
        for l in range(size):
            t.circle(10)
            t.left(360/numbers)
        # Fourth Rosette
        t.penup()
        t.setpos(a, -b)
        t.pendown()
        for l in range(size):
            t.circle(10)
            t.left(360/numbers)
