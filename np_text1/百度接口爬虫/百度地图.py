import requests
import json

# 获取所有拥有公园的城市，并存储至TXT

#!/usr/bin/python
# coding: utf-8

import requests
import json

def getjson(loc):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    pa = {
        'q': '公园',
        'region': loc,
        'scope': '2',
        'page_size': 20,
        'page_num': 0,
        'output': 'json',
        'ak': 'DDtVK6HPruSSkqHRj5gTk0rc'
    }
    r = requests.get("http://api.map.baidu.com/place/v2/search", params=pa, headers= headers)
    decodejson = json.loads(r.text)
    return decodejson

province_list = [
      '河北省', '山西省', '辽宁省', '吉林省', '黑龙江省', '江苏省', '浙江省', '安徽省', '福建省', '江西省', '山东省',
      '河南省', '湖北省', '湖南省', '广东省', '海南省', '四川省', '贵州省', '云南省', '陕西省', '甘肃省', '青海省', '台湾省',
      '内蒙古自治区', '广西壮族自治区', '西藏自治区', '宁夏回族自治区', '新疆维吾尔自治区'
      ]
for exchprovince in province_list:
    decodejson = getjson(exchprovince)
    for eachcity in decodejson['results']:
        city = eachcity['name']
        num = eachcity['num']
        output = '\t'.join([city, str(num)]) + '\r\n'
        with open('cities.txt', 'a+', encoding= 'utf8') as f:
            f.write(output)
            f.close()
decodejson = getjson('全国')
six_cities_list = ['北京市', '天津市', '上海市', '重庆市', '香港特别行政区', '澳门特别行政区']
for eachprovince in decodejson['results']:
    city = eachprovince['name']
    num = eachprovince['num']
    if city in six_cities_list:
        output = '\t'.join([city, str(num)]) + '\r\n'
        with open('cities.txt', 'a+', encoding= 'utf8') as f:
            f.write(output)
            f.close()
