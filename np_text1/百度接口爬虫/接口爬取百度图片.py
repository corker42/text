# -*- coding: utf-8 -*-
import requests
import json
from urllib import request

#构造接口
detail_urls = []
for i in range(0, 130, 30):
    url = "https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8420459241999950641&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%8C%AB&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word=%E7%8C%AB&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&nojc=&pn={}".format(i)
    detail_urls.append(url)

#向接口发送请求

headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#        "Accept":"text/plain, */*; q=0.01",
        "Accept-Encoding":"gzip, deflate, br",
        }

#pic_urls = []
#for detail_url in detail_urls:
#    response = requests.get(detail_url, headers=headers)
#    response.url
#    content = response.content.decode('utf8')
#    
#    #处理json字符串
#    datas = json.loads(content)
#    datas = datas['data']
#    for data in datas:
#        try:
#            pic_url = data['middleURL']
#            pic_urls.append(pic_url)
#        except:
#            continue
#
#num = 0
#for pic_url in pic_urls:
#    path = r"C:\Users\DELL\Desktop\pic\\"
#    path = path + str(num) + '.jpg'
#    request.urlretrieve(pic_url,path)
#    print("第{}张图片下载完成！！".format(num))
#    num += 1


num = 0
for detail_url in detail_urls:
    response = requests.get(detail_url, headers=headers)
    response.url
    content = response.content.decode('utf8')
    
    #处理json字符串
    datas = json.loads(content)
    datas = datas['data']
    for data in datas:
        try:
            pic_url = data['middleURL']
            path = r"C:\Users\sanyuan\Desktop\np_text\百度接口爬虫\pic"
            path = path + str(num) + '.jpg'
            request.urlretrieve(pic_url,path)
            print("第{}张图片下载完成！！".format(num))
            num += 1
        except:
            continue










































































