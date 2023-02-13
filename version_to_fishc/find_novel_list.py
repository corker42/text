from lxml import etree
import requests
from fake_useragent import UserAgent
import json
def FindNovelList():
    url = "http://www.xbiquge.la/xiaoshuodaquan/"

    headers = {
        "User-Agent": UserAgent().chrome
    }
    response = requests.get(url, headers=headers)
    e = etree.HTML(response.text)  # 返回字符串
    #由网页源码而定
    names = e.xpath('//a/text()')
    urls = e.xpath('//a/@href')

    novel_list = []
    novel = {}
    for name,url in zip(names,urls):
        novel[name]=url
        novel_list.append(novel)
        novel = {}
    with open('novel_list.json','w',encoding='utf-8') as f:
        f.write(json.dumps(novel_list,ensure_ascii=False))