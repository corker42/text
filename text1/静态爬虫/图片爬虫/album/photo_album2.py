# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 22:33:37 2021

@author: sanyuan
"""

import requests
import time
def main():
    start = time.time()
    name = ["猫羽�~ 蓝色眼睛女子 尾巴 女孩子 猫耳 猫 可爱二次元动漫4k壁纸",
        "赛博朋克风格奇幻少女 集原美电脑4k壁纸",
"崖上的波妞4k高清壁纸","下午 趴在桌子的女孩4k动漫壁纸","宅女 长筒袜 短发 可爱女孩4k壁纸",
"江南烧酒4k动漫壁纸","车子 少女 女生 绑辫子 唯美好看4k动漫壁纸","百褶裙 校服 黑白袜 学生女孩 动漫美女4k壁纸",
"三个女仆 黑裤袜黑丝美腿 女仆装 沙发 白色透明窗帘 4k动漫壁纸","女子 白色军装制服 黑色丝袜 海边 4k动漫壁纸" ,
"科幻少女 背影 白色衬衫 黑色短裤 美腿4k壁纸" ,"3D绘画 女仆 美腿 黑丝 高跟鞋 两位女仆进门后的一幕 4k动漫壁纸",
"三体智子 和服 武士刀 唯美好看动漫美女4k壁纸","四个女仆 坐地板 黑裤袜 黑丝美腿 房间 沙发 4k动漫壁纸",
"长发少女黑色吊带裙 好看的4k动漫美女壁纸","女孩喝啤酒 飘窗 城市夜景 雨天 猫 好看唯美4k动漫壁纸",
"两位女仆 黑裤袜黑丝 打开门 4k动漫壁纸","肉骨茶 个性动漫美女 骨汤屋 二次元美女 4k动漫壁纸",
"两个女仆 黑色裤袜 美腿 水手服 进门 蜡烛 4k动漫壁纸"
        ]
    right_urls = ["/uploads/allimg/210317/001935-16159115757f04.jpg",
              "/uploads/allimg/210423/224716-16191892361adb.jpg"
"/uploads/allimg/210604/200017-1622808017e3d7.jpg","/uploads/allimg/190824/212516-1566653116f355.jpg",
"/uploads/allimg/200410/213246-1586525566e909.jpg","/uploads/allimg/180803/084010-15332568109b5b.jpg",
"/uploads/allimg/191026/001458-15720200980e55.jpg","/uploads/allimg/210727/000435-1627315475948c.jpg",
"/uploads/allimg/210701/230830-16251521109723.jpg","/uploads/allimg/200216/174956-158184659610a4.jpg",
"/uploads/allimg/210712/183737-1626086257df29.jpg","/uploads/allimg/210512/233947-162083398796f2.jpg",
"/uploads/allimg/210707/235313-16256731939b57.jpg","/uploads/allimg/210528/203909-162220554998dd.jpg",
"/uploads/allimg/200618/005100-1592412660f973.jpg","/uploads/allimg/200511/234750-158921207029df.jpg",
"/uploads/allimg/210318/135851-1616047131c38d.jpg", "/uploads/allimg/210604/232220-16228201403f3c.jpg"        
              ]
    base_url = "https://pic.netbian.com"
    img_urls = list(map(lambda  url: base_url + url,right_urls))
    for i in range(0,17):
        
        headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
              }
        r = requests.get(img_urls[i],headers)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        img_path = 'C:/Users/sanyuan/Desktop/text1' + name[i] + '.jpg'
        with open(img_path,'w',encoding = 'utf8') as fp:
            fp.write(r.text)
            print(name[i], "   ******下载完成！")
            
    end = time.time()  
    print("共耗时" + str(end-start) + "秒")

main()


    

   
    
   
    
   
    
   
    
   
    
   
         