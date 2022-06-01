import re

url = 'https://dytt8.net/html/gndy/dyzz/list_23_29.html'

#爬取前19页
res = re.findall(r'.+/gndy/dyzz/list_23_[1-9].html|.+/gndy/dyzz/list_23_1[0-9].html', url)
print(res)
print(19*25)






