#! /usr/bin/python3
# coding=utf-8
from selenium import webdriver
import time
import re
start = time.time()
url = "http://nt2g03jhyrnomeo0.mikecrm.com/4ixi4Q7"
driver_path = r"C:\chromedriver.exe"
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=driver_path,chrome_options=option)
driver.get(url)
titles = re.findall(r'"t":"(.*?)"',driver.page_source,re.DOTALL)[1:]
contents = driver.find_elements_by_css_selector("input")
details = {
     '姓名':'魏壹鋆',
     '学号':'202004073',
     '专业班级':'应用化学202003',
     "QQ":"2488346986",
     "联系电话":"17882506110",
     "手机":"17882506110",
     "学院":"理学院",
     "文本框":"2222"
          }
print(titles)
i = 0
for content in contents:
    content.send_keys(details[titles[i]])
    i += 1
#提交
driver.find_element_by_xpath("//div[@class='submit']").click()
end = time.time()
print(end - start , 's')


