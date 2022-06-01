# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 21:25:52 2021

@author: sanyuan
"""

from fake_useragent import UserAgent
import requests
url = ""
ua = UserAgent()
headers = {"User-Agent":ua.random}