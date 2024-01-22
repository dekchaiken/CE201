import turtle
leo = turtle.Turtle()
import math
n = 100
def draw_line(t, length,n):
    t.forward(length)
    t.left(360/n)
def polygon(t,length,n):          
    for i in range(n):
        draw_line(t,length,n)
       
def square(t,f):                    
    for i in range(4):
        t.forward(f)
        t.left(90)
 
def line(t,length):
    polygon(t,length,1)
 
def circle(t,r):
    length = ((2*math.pi)*r)/n
    polygon(t,length,n)
 
def hexagon(t,length):
    polygon(leo,100,6)
 
def triangle(t,length):
    polygon(t,length,3)
 
def octagon(t,length):
    polygon(leo,110,8)
 
def arc(t,r,angle):
    a = (n*angle)//360
    for i in range(a):
        length = ((2*math.pi)*r)/n
        draw_line(t, length, n)
 
line(leo,100)
triangle(leo,100)
square(leo,100)  
hexagon(leo,100)
octagon(leo,100)
circle(leo,100)
arc(leo,50,180)
turtle.mainloop()
