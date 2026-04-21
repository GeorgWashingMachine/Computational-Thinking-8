from utils import *


# Section 1 - Variables
# TODO - add starting values for all the variables
x1 =-300
y1 =200
x2 =-300
y2 =60
x3 =-300
y3 =-60
x4 =-300
y4 =-200


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("coalmines")
t1 = create_sprite("notmytempo",x1,y1)
t2 = create_sprite("travisscott",x2,y2)
t3 = create_sprite("dumbcat",x3,y3)
t4 = create_sprite("sisyphus",x4,y4)
# sisyphus is generally fastest, then not my tempo guy, then cat, then fish.
x1c = random.randint(9,17)
x2c = random.randint(6,13)
x3c = random.randint(7,15)
time.sleep(3)
# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
for i in range(45):
     x1 +=x1c
     x2 +=x2c
     x3 +=x3c
     x4 +=random.randint(-3, 8)

     t1.goto(x1, y1)
     t2.goto(x2, y2)
     t3.goto(x3, y3)
     t4.goto(x4, y4)

     window.update()
     time.sleep(0.2)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
s5 = create_sprite("peteer",-200,-200)
s5.color("white")
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    s5.write("tempo guy wins!", font= ("impact", 45, "normal"))
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    s5.write("travis fish wins!", font= ("impact", 45, "normal"))
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    s5.write("dumb cat wins!", font= ("impact", 45, "normal"))
elif x4 >= x1 and x4 >= x3 and x4 >= x2:
    s5.write("sisyphus wins!", font= ("impact", 45, "normal"))

turtle.exitonclick()
