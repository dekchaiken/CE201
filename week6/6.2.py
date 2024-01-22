import turtle
import math
t = turtle.Turtle()
def polygon(t,s):
    for i in range(s):
        t.forward(s)
        t.left(360/s)
def circle(t,r):
    r = ((2*math.pi)*r) / 60
    t.forward(r)
    polygon(t,60)
circle(t,5)
turtle.done()
