import requests
from lxml import etree
import os
import re
from urllib import request

#定义请求头
headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        }
#页面构造
urls = []
for i in range(1,101):
    url = 'https://www.doutula.com/photo/list/?page={}'.format(i)
    urls.append(url)

for url in urls:
    response = requests.get(url, headers=headers)
    content = response.content.decode('utf8')
    #解析
    html = etree.HTML(content)
    #提取数据
    img_urls = html.xpath('//div[@class="page-content text-center"]//a/img/@data-original')
    alts = html.xpath('//div[@class="page-content text-center"]//a/img/@alt')
    for img_url,alt in zip(img_urls,alts):
        suffix = os.path.splitext(img_url)[1]
        alt = re.sub(r'[，。？\|\*]', '', alt)
        img_name = alt + suffix
        request.urlretrieve(img_url, r"C:\Users\wwb\Desktop\pic\\"+ img_name)
        print(img_name + '下载完成！！')







































