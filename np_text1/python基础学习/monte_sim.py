import turtle,random
from  math import sin,pi
from  sys import argv
def f(q):
    return 400 *sin(pi*q/400)
def move(tw, xx, yy):
    s = tw.pen()
    tw.penup()
    tw.goto(xx,yy)
    tw.pen(s)
count = 0
n = 500
t = turtle.Pen()
t.pensize(2)
for _ in range(4):
    t.forward(400)
    t.left(90)
for i in range(401):
    t.goto(i,f(i))
for i in range(n):
    x = random.uniform(0,400)
    y = random.uniform(0,400)
    if y < f(x):
        move(t,x,y)
        t.dot(10,'black')
        count += 1
    else:
        move(t,x,y-5)
        t.circle(5,360)
else:
    print(f'total dots:{n}')
    print(f'inner dots:{count}')
    print('area is {}'.format(400*400*count/n))
t.hideturtle()
turtle.exitonclick()
