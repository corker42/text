# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 11:28:05 2021

@author: sanyuan
"""

from selenium import webdriver
import time
# url = 'https://www.baidu.com/?tn=40020637_5_oem_dg'

# driver_path = r"C:\chromedriver.exe"
# option = webdriver.ChromeOptions()
# driver = webdriver.Chrome(executable_path=driver_path,chrome_options=option)
# driver.get(url)
# input_elt = driver.find_element_by_id('kw')
# input_elt.send_keys('狗')
# time.sleep(3)
# result = driver.find_element_by_id('su')
# result.click()

from selenium.webdriver import ActionChains
driver_path = r"C:\chromedriver.exe"
option = webdriver.ChromeOptions()
browser = webdriver.Chrome(executable_path=driver_path,chrome_options=option)

url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')#切换到iframeResult框架
source = browser.find_element_by_css_selector('#draggable')#找到被拖拽对象
target = browser.find_element_by_css_selector('#droppable')#找到目标
actions = ActionChains(browser)#声明actions对象
actions.drag_and_drop(source, target)
actions.perform()#执行动作
time.sleep(3)
browser.close()


