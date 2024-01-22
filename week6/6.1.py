import turtle
leo = turtle.Turtle()
def polygon(t, length, n):
    for i in range(n):
        t.forward(length)
        t.left(360/n)
def draw_line():
    polygon(leo, 100, 7)
 
draw_line()
