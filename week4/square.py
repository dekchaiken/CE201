import turtle
leo = turtle.Turtle()

def square(t):
    for i in range(4):
        t.forward(100)
        t.left(90)

square(leo)

turtle.mainloop()