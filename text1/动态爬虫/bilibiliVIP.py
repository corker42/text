# -*- coding: utf-8 -*-
# @Author: Null119
# @Desc: { 某vip解析2 }
# @Date: 2022/03/16 12:59

import requests, urllib3, base64, os, time, re
from Crypto.Cipher import AES

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\\|]" # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title) # 替换为下划线
    return new_title

def aesEcbDecode(data, key):
    decrpytBytes = base64.b64decode(data)
    key = bytes(key, encoding='utf-8')
    naes = AES.new(key, AES.MODE_ECB)
    return naes.decrypt(decrpytBytes).decode('utf-8')


def aesEcbEncode(data, key):
    padded = pad_byte(data.encode('utf-8'))
    key = bytes(key, encoding='utf-8')
    naes = AES.new(key, AES.MODE_ECB)
    en_text = naes.encrypt(padded)
    return base64.b64encode(en_text).decode()


def pad_byte(b):
    bytes_num_to_pad = 16 - (len(b) % 16)
    byte_to_pad = bytes([bytes_num_to_pad])
    padding = byte_to_pad * bytes_num_to_pad
    padded = b + padding
    return padded


def enStr(url):
    return aesEcbEncode(url, 'yourme@nxflv@com')


def deStr(enurl):
    return aesEcbDecode(enurl.replace('AINX', ''), 'loveme@nxflv@com')


def proDown(url, path, vtitle, headers):
    if not os.path.exists(path):
        os.mkdir(path)
    start = time.time()
    response = requests.get(url, headers=headers, stream=True, verify=False)
    size = 0
    chunk_size = 1024
    content_size = int(response.headers['content-length'])
    try:
        if response.status_code == 200:
            print('开始下载,[文件大小]:{size:.2f} MB'.format(size=content_size / chunk_size / 1024))
            if vtitle != '':
                filepath = path + vtitle + '.' + os.path.basename(url).split('?')[0].split('.')[1]
            else:
                filepath = path + os.path.basename(url).split('?')[0]
            with open(filepath, 'wb') as file:
                for data in response.iter_content(chunk_size=chunk_size):
                    file.write(data)
                    size += len(data)
                    print('\r' + '[下载进度]:%s%.2f%%' % (
                    '>' * int(size * 50 / content_size), float(size / content_size * 100)), end=' ')
        end = time.time()
        print('\r下载完成!,耗时: %.2f秒' % (end - start))
    except:
        pass


def getVIP(url, arg):
    html = requests.get(url, verify=False).text
    try:
        vTitle = re.search(r'<h1 title="(.*?)">', html).group(1)
        print(f'【{vTitle}】')
    except:
        vTitle = ''

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'Referer': 'https://www.nxflv.com/?url=' + url,
        'Origin': 'https://www.nxflv.com'
    }
    vkey = enStr(url)
    pdat = {
        'url': url,
        'wap': '0',
        'ios': '0',
        'vkey': vkey,
        'type': ''
    }
    html = requests.post('https://www.nxflv.com/Api.php', data=pdat, headers=headers, verify=False)
    enurl = html.json()['url']
    deurl = deStr(enurl)

    print('视频URL：', deurl)
    if int(arg) > 0: proDown(deurl, './',validateTitle(vTitle), headers)


if __name__ == '__main__':
    url = input('请输入url,例如：https://www.bilibili.com/bangumi/play/ep409007/\n')
    getVIP(url, 1)