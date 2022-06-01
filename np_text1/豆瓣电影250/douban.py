from urllib.request import Request, urlopen
import re
"""
爬取豆瓣Top250
目标：排名，评分，名字，评价数
"""
url = 'https://movie.douban.com/top250'
def get_page(url):
    hd = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }
    r = Request(url, headers= hd)
    resp = urlopen(r)
    return resp.read().decode('utf8')
def parser_page(s):
    obj = re.compile(r'<em class="">(?P<rates>.*?)</em>.*?<span class="title">(?P<names>.*?)</span>.*?<span class="rating_num" property="v:average">'
                     r'(?P<commit_nums>.*?)</span>.*?<span>(?P<number>.*?)人评价</span>', re.S)
    res = obj.finditer(s)
    lst = []
    for item in res:
        dic = item.groupdict()
        lst.append(dic)
    return lst


if __name__ == '__main__':
    f = open("move.txt", mode='w', encoding='utf8')
    for i in range(10):
        url = f'https://movie.douban.com/top250?start={i * 25}&filter='
        s = get_page(url)
        result = parser_page(s)
        for d in result:
            f.write(str(d))
            f.write('\n')
        print(result)

