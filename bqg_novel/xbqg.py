import requests
import threading
from lxml import etree
import os

if __name__ == "__main__":
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Referer': 'https://www.xbiquge.la',
            'Cookie': '_abcde_qweasd=0; BAIDU_SSP_lcr=https://www.baidu.com/link?url=jUBgtRGIR19uAr-RE9YV9eHokjmGaII9Ivfp8FJIwV7&wd=&eqid=9ecb04b9000cdd69000000035dc3f80e; Hm_lvt_169609146ffe5972484b0957bd1b46d6=1573124137; _abcde_qweasd=0; bdshare_firstime=1573124137783; Hm_lpvt_169609146ffe5972484b0957bd1b46d6=1573125463',
            'Accept-Encoding': 'gzip, deflate'
        }
    url = 'https://www.xbiquge.la/10/10489/'
    r = requests.get(url,headers=headers)
    r.encoding = r.apparent_encoding
    # print(r.text)
    html = etree.HTML(r.text)
    title_url = html.xpath('//div[@id="list"]/dl/dd/a/@href')
    title_url = ['https://www.xbiquge.la' + i for i in title_url]  # 章节地址
    titlename_list = html.xpath('//div[@id="list"]/dl/dd/a/text()')  # 章节名字列表
    name = html.xpath('//div[@id="info"]/h1/text()')[0]
    print(len(titlename_list), len(title_url))
    for i,url in enumerate(title_url):
        item = {}
        r = requests.get(url, headers=headers)
        r.encoding = r.apparent_encoding
        html = etree.HTML(r.text)
        content_list = html.xpath('//div[@id="content"]/text()')
        content = ''.join(content_list)
        content = content + '\n'
        item['content'] = content.replace('\r\r', '\n').replace('\xa0', ' ')
        item['title'] = titlename_list[i]
        print(titlename_list[i])
        with open(name + '.txt', 'a+', encoding='utf-8') as file:
            file.write(item['title'] + '\n')
            file.write(item['content'])
    print('完成')
