# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 18:06:54 2021

@author: sanyuan
"""

import threading
import random
import time
urls = 100
lock = threading.Lock()
class Producer(threading.Thread):
    def run(self):
        global urls
        
        while True:
            url = random.randint(10, 100)
            lock.acquire()
            urls += url
            print("生产了{}个url,剩余了{}个url".format(url,urls))
            lock.release()
            time.sleep(1)
        
    
    
class Consumer(threading.Thread):
    def run(self):
        global urls
        while True:
            url = random.randint(10, 100)
            lock.acquire()
            urls -= url
            print("消费了{}个url,剩余了{}个url".format(url,urls))
            lock.release()
            time.sleep(1)
        
def multi_thread():
    # 定义生产者线程
    for i in range(5):
        t = Producer()
        t.start()
    
    # 定义消费者线程
    for i in range(2):
        t = Consumer()
        t.start()
multi_thread()    
   
    
    
    
    