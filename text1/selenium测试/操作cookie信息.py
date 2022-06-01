# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 21:48:05 2021

@author: sanyuan
"""
from selenium import webdriver
import time

driver_path = r"C:\chromedriver.exe"

driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://baidu.com/")
cookies = driver.get_cookies()
for cookie in cookies:
            print(cookie)
