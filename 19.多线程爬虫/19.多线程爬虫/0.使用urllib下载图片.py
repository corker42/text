from urllib import request
import os

url = "http://ww2.sinaimg.cn/large/9150e4e5gy1g8trq5uqysj204q02wdfm.jpg"
#split ext:extension
suffix = os.path.splitext(url)[1]
#print(suffix)
request.urlretrieve(url, r"C:\Users\wwb\Desktop\pic\\"+'pic'+suffix)

















