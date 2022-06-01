
from turtle import *

import turtle
t = Turtle()
t.pensize(0.1)
turtle.bgcolor("black")
colors = ["red","yellow","purple","blue"]
t._tracer(False)
for x in range(100):
    t.forward(2*x)

    t.color(colors[x % 4])

    t.left(91)

t._tracer(True)
done()
