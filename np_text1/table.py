# def cut(len,k):
#     k = min(len,k)
#     if len == 0 or k == 1:
#         return 1
#     else:
#         print(k)
#         return cut(len-k,k) + cut(len,k-1)
#
# cut(6,3)
# from functools import lru_cache
# @lru_cache()
# def fib(n):
#     if n ==1 or n ==2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# import  time
# strt = time.time()
# print(fib(40))
# end = time.time()
# print(end - strt)

# L = [2,5,3,6]
# it = iter(L)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# def fib():
#     a,b = 0,1
#     while True:
#         yield b
#         a,b = b,a+b
# g = fib()
# for i in range(120):
#     print(next(g))

# f = []
# print(gets)
# s = [1,5,7,9,14]
# y = s
# y.append(55)
# d = s.copy()
# d.append(3)
# print(s,d,y)
import requests,re
from lxml import etree
base_url = 'https://www.bbiquge.net/book_133303/56614649.html'
headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Referer":"https://www.bbiquge.net/",
        "Cookie":"Hm_lvt_cc13cd690e17410a96647c14d9e29aba=1644113098; Hm_lvt_a6e0e6155afbc85db439c009f957f6d4=1644113098; jieqiVisitTime=jieqiArticlesearchTime%3D1644114148; jieqiVisitId=article_articleviews%3D12613%7C24879; PHPSESSID=rppphnuqdigg83k8fg56re8428; jieqiUserInfo=jieqiUserId%3D52037%2CjieqiUserName%3D%D4%AA%2CjieqiUserGroup%3D3%2CjieqiUserName_un%3D%26%23x5143%3B%2CjieqiUserLogin%3D1644116556; jieqiVisitInfo=jieqiUserLogin%3D1644116556%2CjieqiUserId%3D52037; Hm_lpvt_cc13cd690e17410a96647c14d9e29aba=1644116563; Hm_lpvt_a6e0e6155afbc85db439c009f957f6d4=1644116563",
        "Accept-Encoding":"gzip, deflate, br",
        }
response = requests.get(url=base_url)
response.encoding = response.apparent_encoding
content = response.text
html = etree.HTML(content)
# obj = re.compile('<dd><a href="(?P<novel_urls>.*?)">(?P<titles>.*?)</a></dd>',re.S)
# result = obj.finditer(content)
# for it in result:
#     print(it.group("novel_urls"),it.group("titles"))
# print(content)
# quanwen =  html.xpath('//div[@id="content"]/text()')
# # quanwen = etree.tostring(quanwen).decode('utf8')
# quanwen = '\n'.join(quanwen)
# quanwen =quanwen.strip().replace('\r\r', '\n').replace('\xa0', '')
# with open('1.txt',mode='w',encoding='utf8') as f:
#         f.write(quanwen)











