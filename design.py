import turtle
import math

t = turtle.Turtle()
t.speed(100)
t.color("red", "blue")
                 
t.begin_fill()
for i in range(0, 5000):
    t.forward(math.sqrt(i) * 15)
    t.left(185)


t.end_fill()


turtle.done()
