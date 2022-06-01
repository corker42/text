import turtle
from math import sin,pi
def drawline(t,x1,y1,x2,y2):
    s = t.pen()
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.goto(x2,y2)
    t.pen(s)
def move(t,x,y):
    s = t.pen()
    t.penup()
    t.goto(x,y)
    t.pen(s)
def func(x):
    return 200 * sin(pi*x/100) + 200
t = turtle.Pen()
t.pensize(2)
#绘制坐标轴
drawline(t,-20,0,410,0)
drawline(t,0,-20,0,410)
#绘制正弦曲线
move(t,0,func(0))
for i in range(1,400):
    t.goto(i,func(i))
#隐藏绘图笔
t.hideturtle()
turtle.exitonclick()