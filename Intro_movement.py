import time, turtle, random
from utils import *
# Section 1: Setup
set_background("coalmines")
s1 = create_sprite("lebron(1)",-100,0)
s2 = create_sprite("notmytempo",100,0)

# Section 2: define controls
def move_up():
    x = s1.xcor()
    y = s1.ycor()
    s1.goto(x, y+10)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor()
    s1.goto(x, y-10)
    
def move_left():
    x = s1.xcor()
    y = s1.ycor() 
    s1.goto(x-10, y)
    
def move_right(): 
    x = s1.xcor()
    y = s1.ycor() 
    s1.goto(x+10, y)

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")
def move_up2():
    x = s2.xcor()
    y = s2.ycor()
    s2.goto(x, y+10)
        
def move_down2():
    x = s2.xcor()
    y = s2.ycor()
    s2.goto(x, y-10)
    
def move_left2():
    x = s2.xcor()
    y = s2.ycor() 
    s2.goto(x-10, y)
    
def move_right2(): 
    x = s2.xcor()
    y = s2.ycor() 
    s2.goto(x+10, y)

window.onkeypress(move_up2, "Up")
window.onkeypress(move_down2, "Down")
window.onkeypress(move_left2, "Left")
window.onkeypress(move_right2, "Right")

# Section 3: define other controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")
def draw():
    s1.pendown()
    s2.pendown()
def stop_drawing ():
    s1.penup()
    s2.penup()
def erase ():
    s1.clear()
    s2.clear()
def red_pen ():
    s1.color("red")
    s2.color("red")
def green_pen ():
    s1.color("green")
    s2.color("green")
def black_pen():
    s1.color("black")
    s2.color("black")
def white_pen():
    s1.color("white")
    s2.color("white")
def reset (x,y):
    s1.goto(x,y)
    s2.goto(x,y)
window.onscreenclick(reset)
window.onkeypress(red_pen,"r")
window.onkeypress(green_pen,"g")
window.onkeypress(black_pen,"b")
window.onkeypress(erase,"e")
window.onkeyrelease(stop_drawing,"q")
window.onkeypress(draw,"q")
window.onkeypress(white_pen,"p")
# Section 4: game loop
window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()