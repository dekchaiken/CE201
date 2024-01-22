import turtle
leo = turtle.Turtle()

def square(t,length):
    for i in range(4):
        t.forward(length)
        t.left(90)

square(leo, 100)

turtle.mainloop()