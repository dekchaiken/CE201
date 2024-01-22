import turtle
leo = turtle.Turtle()

def polygon(t, length, n):
    for i in range(n):
        t.forward(length)
        t.left(360/n)

def circle(t,r):
    polygon(t, 6, r)

circle(leo,50)

turtle.mainloop()