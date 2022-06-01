
from turtle import *
from random import *
from math import *

def drawTree(n, l):
    pd()
    # 阴影效果
    t = cos(radians(heading() + 45)) / 8 + 0.25
    pencolor(t, t, t)
    pensize(n / 3)

    # 画树枝
    forward(l)
    if n > 0:
        # 右分支偏转角度
        b = random() * 15 + 10

        # 左分支偏转角度
        c = random() * 15 + 10

        # 下一个分支的长度
        d = l * (random() * 0.35 + 0.6)

        # 右转一定角度，画右分支
        right(b)
        drawTree(n - 1, d)

        # 左转一定角度，画左分支
        left(b + c)
        drawTree(n - 1, d)

        # 转回来
        right(c)
    else:
        right(90)
        n = cos(radians(heading() - 45)) / 4 + 0.5
        pencolor(n, n * 0.8, n * 0.8)
        circle(3)
        left(90)

        # 添加0.3倍的飘落叶子
        if(random() > 0.7):
            pu()
            # 飘落
            t = heading()
            an = -40 + random()*40
            setheading(an)
            dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
            forward(dis)
            setheading(t)


            # 画叶子
            pd()
            right(90)
            n = cos(radians(heading() - 45)) / 4 + 0.5
            pencolor(n*0.5+0.5, 0.4+n*0.4, 0.4+n*0.4)
            circle(2)
            left(90)
            pu()

            #返回
            t = heading()
            setheading(an)
            backward(dis)
            setheading(t)

    pu()
    backward(l)

bgcolor(0.5, 0.5, 0.5)
ht()
speed(0)
tracer(0, 0)
pu()
backward(100)
left(90)
pu()
backward(300)
drawTree(12, 100)
done()
