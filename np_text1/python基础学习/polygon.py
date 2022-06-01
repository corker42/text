#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from  math import sin,pi
import  turtle
n = 8
d = 300
t = turtle.Pen()
t.pensize(2)
#绘制多边形
for _ in range(n):
    t.forward(d*sin(pi/n))
    t.left(360/n)
t.hideturtle()
turtle.exitonclick()