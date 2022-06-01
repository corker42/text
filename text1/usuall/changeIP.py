# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 22:11:06 2021

@author: sanyuan
"""

import socket
import socks
import requests

socks.set_default_proxy(socks.SOCKS5,"127.0.1.1",9150)
socket.socket = socks.socksocket
a = requests.get("http://checkip.amazonaws.com").text
print(a)