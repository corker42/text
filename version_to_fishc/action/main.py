import os
from lxml import etree

if __name__ == '__main__':
    path = r"C:\Users\sanyuan\Desktop\version_to_fishc\books\我有一座恐怖屋\chapters"
    chapters = os.listdir(path)
    c_names = [(str(chapter).split(":", 1))[0][1:-5] for chapter in chapters]
    paixu = [(str(chapter).split(" "))[0][1:-1] for chapter in chapters]
    book_chapters = [path + "\\" + x for x in chapters]
    count = 1
    while(count<1250):
        if(count==117):
            count += 1
        suoyi = paixu.index(str(count))
        book_chapter = book_chapters[suoyi]
        c_name = c_names[suoyi]
        with open(book_chapter, 'r', encoding="utf8") as f:
            content = f.read()
        html = etree.HTML(content)
        body_content = html.xpath('//div[@id = "content"]/text()')
        body = ''
        for i in body_content:  # 先拼接
            if i != '\n':
                i = repr(i).replace(r'\xa0', '').replace("'", '')
                body += i
        body = repr(body).replace("\\n", '\n').replace('\\', '')  # 最终处理
        with open(r"C:\Users\sanyuan\Desktop\version_to_fishc\action\我有一座恐怖屋.txt",'a+',encoding='utf8') as f1:
            f1.write('\n\n')
            f1.write(c_name)
            f1.write('\n\n')
            f1.write(body)
        count += 1


