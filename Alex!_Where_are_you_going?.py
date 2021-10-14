#My friend, Alex can't stick to something :,D

import turtle
import random as rdm

def tomorrow_is_a_new_day(alex):
    rcol1 =rdm.random()
    rcol2 =rdm.random()
    rcol3 =rdm.random()
    alex.pencolor(rcol1,rcol2,rcol3)
    for i in range(20):
        angle=rdm.randrange(1,360)
        alex.right(angle)
        steps=rdm.randrange(1,180)
        alex.forward(steps)
  

wn = turtle.Screen()
alex = turtle.Turtle()


alex.speed(5)
alex.shape("turtle")
alex.pensize(5)
bed = alex.position()


for i in range(20):
    alex.goto(bed)    
    alex.down()  
    tomorrow_is_a_new_day(alex)
    alex.up()
wn.exitonclick()
