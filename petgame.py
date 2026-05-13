from utils import *
#GOAL of the game is to keep tempo guy happy and alive 
# Section 1 - setup
# TODO - set a background using set_background()
set_background("symphony")
m1 = create_sprite("alien", -350,50)
m1.hideturtle()
# TODO - create at least two variables and set their starting value. ex: cookies = 0
happiness = 100
tempos = 70
age = 0
multipliers = 1
scaling = 0
price = 50
# Section 2 - controls
# TODO - define an action. ex: def my_control()
t1 = create_sprite("notmytempo",0,-300)
# this one adds tempo point based on the multiplier you have
def get_tempo ():
    global tempos, multipliers
    tempos += multipliers
# this one makes the tempo man talk based off how happy he is
def talk ():
    global happiness
    t1.clear()
    if tempos >= 50:
        t1.write("good tempo", font=("arial", 30,"normal"))
    else :
        t1.write("not quite my tempo", font=("arial", 30,"normal"))
#this one lets you buy tempo multipliers if you have 50 tempos but the price doubles everytime you buy it
def buymult ():
    global multipliers, tempos, price
    if tempos >= price :
        multipliers += 1
        tempos -= price
        price = 2*price
# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")
window.onkeyrelease(get_tempo, "t")
# TODO - make a second control
window.onkeypress(talk, "space")
window.onkeypress(buymult, "r")
# Section 3 - game loop
time.sleep (1)
window.listen()
for i in range(1000000000):
    # TODO - put any automatic actions here
    if i % 20 == 0:
        if happiness < 100:
            if tempos > 50:
                happiness += 1
    if i % 5 == 0:
        if tempos < 50:
            if happiness > -1:
                happiness -= 1
    if i % 40 == 0:
        if tempos >= 1:
            tempos -= scaling
        else:
            tempos = 0
    if i % 500 == 0:
        scaling += 1
    if i % 500 == 0:
        age += 1
    if i % 30 == 0:
        wander = random.randint(-40,40)
        t1.goto (wander,0)
    # OPTIONAL - use the message sprite to say a message
    m1.clear ()
    m1.write(f"tempos: {tempos}\nhappiness: {happiness}\nage: {age}\nmult: {multipliers}\nprice: {price}", font=("arial", 30,"normal"))
    if happiness == 0:
        break
    time.sleep(0.01)
    window.update()