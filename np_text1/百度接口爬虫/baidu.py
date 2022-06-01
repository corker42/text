import requests
import json
from urllib import request
def get_pic(url,name):
    path = r"C:\Users\sanyuan\Desktop\np_text\百度接口爬虫\pic\\"
    path = path + str(name) + '.jpg'
    request.urlretrieve(url, path)
def get_info(detail_urls):
    name = 1
    hd = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Accept-Encoding":"gzip, deflate, br",
        }
    for detail_url in detail_urls:
        r = requests.get(url=detail_url,headers=hd)
        content = r.content.decode('utf8')
        datas = json.loads(content)
        datas = datas['data']
        for data in datas:
            try:
                img_url = data['middleURL']
                get_pic(url=img_url, name=name)
                print(f'第{name}张图片下载完成！！')
                name += 1
            except:
                continue
if __name__ == '__main__':
    detail_urls = []
    for i in range(1, 11):
        url = f'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=9033073397045929072&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E7%BE%8E%E5%A5%B3&cg=girl&queryWord=%E7%BE%8E%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn={i * 30}'
        detail_urls.append(url)
    get_info(detail_urls)

