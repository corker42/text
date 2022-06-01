# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 20:06:54 2021

@author: sanyuan
"""

import urllib   
import requests

def get_url():
    url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn=1&rn=30&reqId=ec2404f0-47f3-11ea-b35a-df5b093dd227'.format(new)
    response = requests.get(url, headers=headers).json()
    return response

def get_url_data():
    rids = []
    jsons = get_url()
    lists = jsons['data']['list']
    for i in lists:
        rids.append((i['rid'],i['name']))
    return rids

def download_mp3():
    for i in get_url_data():
        url = 'http://www.kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3'.format(str(i[0]))
        response = requests.get(url, headers=headers).json()
        html = response['url']
        data = requests.get(html).text
        with open('酷我音乐爬取\{}-{}.mp3'.format(test, i[1]), 'wb') as f:
            f.write(data)
            print('下载完成{}'.format(i[1]))

if __name__ == '__main__':
    test = str(input('请输入想要下载的歌手：'))
    new = urllib.parse.quote(test)
    headers = {
        'Referer': 'http://www.kuwo.cn/search/list?key={}'.format(new),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'csrf': 'NZNCXJFZLFF',
        'Host': 'www.kuwo.cn',
        'Cookie': '_ga=GA1.2.172942019.1580702894; _gid=GA1.2.771718281.1580890479; uname3=%u3081%u3044%u305F%u3093%u3066%u3044%u3053%u306A%u3093; t3kwid=235511292; userid=235511292; websid=2033651825; pic3="http://q.qlogo.cn/qqapp/100243533/BEB10B9B72AB7C5E6700E08B820BA1C5/100"; t3=qq; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1580702894,1580890479,1580891122; _gat=1; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1580892336; kw_token=NZNCXJFZLFF'
    }

    download_mp3()
