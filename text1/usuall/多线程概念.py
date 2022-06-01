# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time
import threading
# def lisen():
#     for i in range(3):
#         print('正在听音乐{}。。。'.format(i))
#         time.sleep(1)
        
# def dowmload():
#     for i in range(3):
#         print('正在下载音乐{}。。。'.format(i))
#         time.sleep(1)        

# def single_thread():
#     lisen()
#     dowmload()

# single_thread()        
    
# def multi_thread():
#     t1 = threading.Thread(target = lisen)
#     t2 = threading.Thread(target = dowmload)
    
#     t1.start()
#     t2.start()
# multi_thread()
# class Lisen_thread(threading.Thread):
#     def run(self):
#         for i in range(3):
#             print('正在听音乐{}。。。'.format(threading.current_thread()))
#             time.sleep(1)

# class doenload_thread(threading.Thread):
#     def run(self):
#         for i in range(3):
#             print('正在下载音乐{}。。。'.format(threading.current_thread()))
#             time.sleep(1)   

# def multi_thread():
#     t1 = Lisen_thread()
#     t2 = doenload_thread()
#     t1.start()
#     t2.start()
# multi_thread()    
    
# print(len(threading.enumerate()))    
# lock = threading.Lock()
# num = 0
# def add_num1():
#     global num
#     lock.acquire()
#     for i in range(1000000):        
#         num += 1
#     lock.release()
#     print('num1 是{}'.format(num))

# def add_num2():
#     global num
#     lock.acquire()
#     for i in range(1000000):        
#         num += 1
#     lock.release()
#     print('num2 是{}'.format(num))

# def multi_thread():
#     t1 = threading.Thread(target = add_num1)
#     t2 = threading.Thread(target = add_num2)
#     t1.start()
#     t2.start()

# multi_thread()

 
        
       
     
        
        
        
        
        
        
        
        
        