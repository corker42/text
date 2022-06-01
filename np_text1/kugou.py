
import requests
import re
# 通过第一个url获取album_audio_id， album_id，hash
# 然后将获取的参数传入第二个url,获取真正的下载链接并下载
print('请输入歌曲名称:',end='')
song_name = input()
path = r'C:\Users\sanyuan\Desktop\\' + song_name + '.mp3'
url = f"http://msearchcdn.kugou.com/api/v3/search/song?showtype=14&highlight=em&pagesize=30&tag_aggr=1&tagtype=%E5%85%A8%E9%83%A8&plat=0&sver=5&keyword={song_name}&correct=1&api_ver=1&version=9108&page=1&area_code=1&tag=1&with_res_tag=1"
r = requests.get(url).text
com1 = re.compile('"sqhash":"(.*?)"', re.S)
com2 = re.compile('"album_id":"(.*?)"', re.S)
hash1 = com1.findall(r)[1]
album_id = com2.findall(r)[1]
print(hash1,album_id)
url1 = f'https://www.kugou.com/song/#hash={hash1}&album_id={album_id}'
print(url1)
r = requests.get(url=url1).text
com3 = re.compile('src="(.*?).mp3"', re.S)
reall_url = com3.findall(r)[0]
# reall_url = reall_url + '.mp3'
print(reall_url)
# 第二个 "http://trackercdnbj.kugou.com/i/v2/?album_audio_id=99121191&behavior=play&cmd=25&album_id=44746292&hash=b74709ac805089efe8e814ba73db9702&userid=0&pid=2&version=9108&area_code=1&appid=1005&key=407732fc325852538ca836581fe4e370&pidversion=3001&with_res_tag=1"