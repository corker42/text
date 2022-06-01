# import requests,os
# from lxml import etree
# # url = 'https://www.jdlingyu.com/wp-content/uploads/2021/08/163323ckjfjmjj0kv7mjvz.jpg'
# #
# # print(os.getcwd())
# # # path = os.mkdir("file")
# # r = requests.get(url)
# # with open(file+ '\\' + '1.jpg',mode='wb') as f:
# #     f.write(r.content)
# # file = 'sss'
# # os.mkdir(file)
# # path = os.path.abspath(file) + '\\'
# # print(path)
# url = 'https://www.jdlingyu.com/96538.html'
# r = requests.get(url)
# r.encoding = 'utf8'
# html = etree.HTML(r.content)
# img_urls = html.xpath('//div//p/img/@src')
# for i,img_url in enumerate(img_urls):
#     print(i,img_url)
# def hailuota(n,a,b,c):
#     if n > 0:
#         hailuota(n-1,a,c,b)
#         print(f"从{a}移动到{c}")
#         hailuota(n-1,b,a,c)
# hailuota(7,'A','B','C')
# i = 0
# def func():
#     global i
#     print(i)
#     i += 1
#     func()
# func()
