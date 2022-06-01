# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 19:53:00 2021

@author: sanyuan
"""

from queue import Queue
import threading
import time

# # 实例化Q队列
# q = Queue(4)

# # 判断Q队列是否为空
# print(q.empty())
# # 放一个数据到Q队列中
# q.put(0)
# q.put(0)
# q.put(0)
# q.put(0)

# # 判断队列是否为空
# print(q.empty())
# # 判断队列是否满了
# print(q.full())
# # 判断队列长度
# print(q.qsize())
# # 打印队列数据
# for i in range(q.qsize()):
#     print(q.get())
"""
.put(block=True):向队列内添加数据
.get(block=True):获取队列内的数据
block ->>指操作是否是阻塞式的
"""

q = Queue(5)

def add_num(q):
    num = 0
    while True:
        q.put(num)
        num += 1
        time.sleep(3)
def get_num(q):
    while True:
        print(q.get())
        
t1 = threading.Thread(target=add_num,args=[q])
t2 = threading.Thread(target=get_num,args=[q])

t1.start()
t2.start()































