import time
from concurrent.futures import ThreadPoolExecutor
import requests,os
from lxml import etree

def getHTML(url):
    hd = {
         "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Referer":"https://www.jdlingyu.com/"
       }
    r = requests.get(url,headers=hd)
    r.encoding = r.apparent_encoding
    return r
def get_link():
    urls = []
    for i in range(1,5):
        url = f'https://www.jdlingyu.com/tag/清纯少女/page/{i}'
        r = getHTML(url)
        html = etree.HTML(r.text)
        link = html.xpath('//ul//li/div/div[1]/a/@href')
        # print(link)
        urls.append(link)
    return urls
def download_onepage(url):
    r = getHTML(url)
    html = etree.HTML(r.text)
    img_urls = html.xpath('//div//p/img/@src')
    file_name = html.xpath('//div//header/h1/text()')[0]
    os.mkdir(file_name)
    path = os.path.abspath(file_name) + '\\'
    for i,img_url in enumerate(img_urls):
        r = getHTML(url=img_url)
        with open(path + str(i) + '.jpg',mode='wb') as f:
            f.write(r.content)
    print(file_name + '下载完毕')

if __name__ == '__main__':
    s = time.time()
    real_urls = []
    urls = get_link()
    for i in urls:
        for real_url in i:
            real_urls.append(real_url)
    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        for url in real_urls:
            t.submit(download_onepage,url)
    e = time.time()
    print('全部下载完毕,用时' + str(float(e-s)/60) + '分钟')
    # for url in real_urls:
    #     download_onepage(url)
    # print('全部下载完毕')


















