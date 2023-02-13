import tkinter as tk
from tkinter import scrolledtext
import requests
from lxml import etree
def reval(titlename):
    name = titlename + '下载成功\n'
    return name
def download_1(url):
    pass
def download_2(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'Referer': 'https://www.xbiquge.la',
        'Cookie': '_abcde_qweasd=0; BAIDU_SSP_lcr=https://www.baidu.com/link?url=jUBgtRGIR19uAr-RE9YV9eHokjmGaII9Ivfp8FJIwV7&wd=&eqid=9ecb04b9000cdd69000000035dc3f80e; Hm_lvt_169609146ffe5972484b0957bd1b46d6=1573124137; _abcde_qweasd=0; bdshare_firstime=1573124137783; Hm_lpvt_169609146ffe5972484b0957bd1b46d6=1573125463',
        'Accept-Encoding': 'gzip, deflate'
    }
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding
    # print(r.text)
    html = etree.HTML(r.text)
    title_url = html.xpath('//div[@id="list"]/dl/dd/a/@href')
    title_url = ['https://www.xbiquge.la' + i for i in title_url]  # 章节地址
    titlename_list = html.xpath('//div[@id="list"]/dl/dd/a/text()')  # 章节名字列表
    name = html.xpath('//div[@id="info"]/h1/text()')[0]
    for i, url in enumerate(title_url):
        item = {}
        r = requests.get(url, headers=headers)
        r.encoding = r.apparent_encoding
        html = etree.HTML(r.text)
        content_list = html.xpath('//div[@id="content"]/text()')
        content = ''.join(content_list)
        content = content + '\n'
        item['content'] = content.replace('\r\r', '\n').replace('\xa0', ' ')
        item['title'] = titlename_list[i]
        reval(titlename_list[i])
        with open(name + '.txt', 'a+', encoding='utf-8') as file:
            file.write(item['title'] + '\n')
            file.write(item['content'])
window = tk.Tk()
window.title('小说下载器')
window.geometry('500x500')
def choice_download():
    s = var.get()
    return s
def run():
    url = e.get()
    s = choice_download()
    if s == 'A':
        download_1(url)
    if s == 'B':
        download_2(url)
var = tk.StringVar()
r1 = tk.Radiobutton(window, text='笔趣阁',
                    variable=var, value='A',
                    command=choice_download)
r1.pack()
r2 = tk.Radiobutton(window, text='新笔趣阁',
                    variable=var, value='B',
                    command=choice_download)
r2.pack()
e = tk.Entry(window, show=None)
e.pack(padx=100, pady=20)
b = tk.Button(window, text='开始下载', width=10,
              height=1, command=run)
b.pack()
scr = scrolledtext.ScrolledText(window, width=30, height=5, wrap=tk.WORD)
scr.pack()

window.mainloop()