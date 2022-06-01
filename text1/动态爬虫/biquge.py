# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 22:17:02 2021

@author: sanyuan
"""
import requests, threading
from lxml import etree
from queue import Queue

class Novel(threading.Thread):
    def __init__(self, novelurl_list=None, name_list=None):
        super().__init__()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Referer': 'http://www.xbiquge.la/7/7931/',
            'Cookie': '_abcde_qweasd=0; BAIDU_SSP_lcr=https://www.baidu.com/link?url=jUBgtRGIR19uAr-RE9YV9eHokjmGaII9Ivfp8FJIwV7&wd=&eqid=9ecb04b9000cdd69000000035dc3f80e; Hm_lvt_169609146ffe5972484b0957bd1b46d6=1573124137; _abcde_qweasd=0; bdshare_firstime=1573124137783; Hm_lpvt_169609146ffe5972484b0957bd1b46d6=1573125463',
            'Accept-Encoding': 'gzip, deflate'
        }
        self.novelurl_list = novelurl_list
        self.name_list = name_list
