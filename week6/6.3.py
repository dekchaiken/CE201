import turtle
import math
leo=turtle. Turtle()
side=60
def draw_line(t, length,side):
    t.forward(length)
    t.left(360/side)
def arc(t,r,angle):
    a = side*angle//360
    for i in range (a):
        length= ((2*math.pi)*r)/side
        draw_line(t, length, side)
arc(leo,100,180)
turtle.mainloop()
