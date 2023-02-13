import requests
from lxml import etree


def getHTML(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'accept - encoding': 'gzip, deflate, br',
        'referer': 'https://cn.bing.com/'
    }
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding
    html = etree.HTML(r.text)
    return html
if __name__ == '__main__':
    url = 'https://www.shuquge.com/txt/81316/index.html'
    html = getHTML(url=url)
    title_list = html.xpath('//div[@class="listmain"]/dl/dd/a/text()')
    title_url = html.xpath('//div[@class="listmain"]/dl/dd/a/@href')
    title_url = ['https://www.shuquge.com/txt/81316/' + i for i in title_url]
    name = html.xpath('//div[@class="info"]//h2/text()')[0]
    print(len(title_url), len(title_list))
    for i, url in enumerate(title_url):
        html = getHTML(url)
        content = html.xpath('//div[@id="content"]/text()')
        content = ''.join(content)
        content = content.replace('\r\r', '\n').replace('\xa0', ' ')
        print(title_list[i])
        with open(name + '.txt', 'a+', encoding='utf-8') as file:
            file.write(title_list[i])
            file.write(content)
    print('完成')
