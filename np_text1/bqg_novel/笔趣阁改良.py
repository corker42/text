import requests
import os,re
from bs4 import BeautifulSoup
import threading,queue
def download_one(url,dir_path):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    chapter_soup = BeautifulSoup(r.text, "html.parser")
    content_tag = chapter_soup.div.find(id="content")
    name = chapter_soup.div.h1.text
    content_text = content_tag.text.replace('\xa0', '\n')
    # content_text = ''.join(content_text)
    # print(content_text,name)
    with open(dir_path + '\\' + name + '.txt',mode='w',encoding='utf8') as f:
        f.write(content_text)
def createfile(url,save_path):
    r = requests.get(url)
    r.encoding = 'gbk'
    content = r.text
    novel_name = re.search('<div id="info">.*?<h1>(.*?)</h1>', content, re.DOTALL)[0]
    novel_name = novel_name.split('<h1>')[-1].split('</h1>')[0]
    dir_path = save_path + '\\' + novel_name
    if not os.path.exists(dir_path):
        os.path.join(save_path, novel_name)
        os.mkdir(dir_path)
    real_urls = re.findall('<dd><a href="(.*?)"', content, re.DOTALL)
    real_urls = [base_url + x for x in real_urls ]
    return real_urls,dir_path
if __name__ == "__main__":
    base_url =  'https://www.biqugee.com'
    url = 'https://www.biqugee.com/book/30570/'
    save_path = r'C:\Users\sanyuan\Desktop\np_text1\bqg_novel'
    real_urls,dir_path = createfile(url,save_path)
    # q_queue = queue.Queue()
    for real_url in real_urls:
        # q_queue.put(real_url)
        # t1 = threading.Thread(download_one, args=(real_url, dir_path))
        # t2 = threading.Thread(download_one, args=(real_url, dir_path))
        # t1.start()
        # t2.start()
        download_one(real_url,dir_path)










