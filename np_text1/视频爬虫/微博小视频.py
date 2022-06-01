# https://www.kuaishou.com/graphql
import requests
from lxml import etree
url = 'https://f.video.weibocdn.com/u0/rBvyGB9xgx07TBLvMP44010412068Z9M0E030.mp4?label=mp4_1080p&template=1920x1012.25.0&trans_finger=d88af6227b88881484d2b59dfbafa136&media_id=4734763261689877&tp=8x8A3El:YTkl0eM8&us=0&ori=1&bf=3&ot=h&ps=3lckmu&uid=8oDWXt&ab=3915-g1,6377-g0,1192-g0,1258-g0,3601-g0&Expires=1644485783&ssig=gV7rWXLMBJ&KID=unistore,video'
hd = {
         "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Referer":"https://weibo.com/",
        "Accept-Encoding": "gzip, deflate, br"
       }
# data = json.dumps(data)
r = requests.get(url=url)
r.encoding = r.apparent_encoding
# video_url = html.xpath('//*[@id="wbpv_video_467_html5_api"]/@src')# http://t.cn/A6ilGR6b
with open('2.mp4','wb') as f:
    f.write(r.content)

# 228908 90268404
# https://sr-sycdn.kuwo.cn/b639ccbcfb3d79b103cc10c951282469/6205badf/resource/n2/76/17/3758654580.mp3
# https://sr-sycdn.kuwo.cn/a0dc1f42efb382ea72dad3c2ef1497a1/6205bcba/resource/n2/76/17/3758654580.mp3
# https://sr-sycdn.kuwo.cn/6da3adbf3d9c2e934c648cf98d0d6ec4/6205bd32/resource/n2/76/17/3758654580.mp3
# b460ed971e30648dce388ef99aeb035f
