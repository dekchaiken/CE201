import turtle
leo = turtle.Turtle()

def polygon(t, length, n):
    for i in range(n):
        t.forward(length)
        t.left(360/n)
polygon(leo, 100, 3)

turtle.mainloop()