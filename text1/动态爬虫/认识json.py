# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 22:26:05 2021

@author: sanyuan
"""

"""
本质：一个字符串，自由度较高
字典："{"name":"peter","age":"20","job":"teacher"}"
"""

import json
import requests
import random
# data = {"name":"peter","age":"20","job":"teacher"}

# json_str = json.dumps(data)
# print(type(json_str))

# data1 = json.loads(json_str)
# print(data1)


url ="http://output.nsfc.gov.cn/baseQuery/data/conclusionQueryResultsData"
user_agent_list = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/61.0",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
                    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
                    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
                    ]
headers = {
    "User-Agent":"",
    "Referer":"http://output.nsfc.gov.cn/projectQuery",
    "Content-Type":"application/json",
    "Cookie":"JSESSIONID=56219EED1588B53381BF67DCB17E3AFA; a923a4ac2d19738eSTATUS=0000000163194a15402e6c4b2648ebc9af8d634127050721436d8fa9cbe5; 422a2071aec8d583EVENT=cbe51412705ebc9af8d6",
    "Host":"output.nsfc.gov.cn",
    "Origin":" http://output.nsfc.gov.cn"
    }
headers["User-Agent"] = random.choice(user_agent_list)
data = {"ratifyNo":"","projectName":"","personInCharge":"","dependUnit":"",
        "code":"G01","projectType":"218","subPType":"","psPType":"","keywords":"",
        "ratifyYear":"","conclusionYear":"2017","beginYear":"","endYear":"",
        "checkDep":"","checkType":"","quickQueryInput":"","adminID":"","pageNum":0,
        "pageSize":5,"queryType":"input","complete":"true"}
data = json.dumps(data)

r = requests.get(url,headers,data = data)
content = r.content.decode('utf8')
print(r.status_code)
print(content)


