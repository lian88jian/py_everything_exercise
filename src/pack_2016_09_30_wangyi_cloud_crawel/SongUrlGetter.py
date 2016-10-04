'''
Created on 2016年9月30日

@author: lianjian
'''
import httplib2
from urllib.parse import urlencode
import json as JsonObject
from src.pack_2016_09_30_wangyi_cloud_crawel.PostEncoder import encrypted_request


class SongUrlGetter(object):
    '''
    classdocs
    '''


    def __init__(self, obj):
        self.http = httplib2.Http();
        self.obj = obj;
        
    def getSongUrl(self):
        response = self.http.request(
            uri='http://vip.mrabit.com/get_music163.php', 
            method='POST',
            body= urlencode({
                'url':self.obj['id']
                }),
            headers={
                'Accept':'*/*',
                'Accept-Encoding':'gzip, deflate',
                'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
                'Cache-Control':'no-cache',
                'Connection':'keep-alive',
                'Content-Length':'10',
                'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie':'__cfduid=de6b1f16402977e0c56ac9ff43839e62b1475215644; CNZZDATA1257134228=904778590-1475213997-http%253A%252F%252Fwww.52pojie.cn%252F%7C1475219408; _yd_=GA1.3.1250531416.1475215647',
                'Host':'vip.mrabit.com',
                'Origin':'http://vip.mrabit.com',
                'Pragma':'no-cache',
                'Referer':'http://vip.mrabit.com/music163.php',
                'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
                'X-Requested-With':'XMLHttpRequest'
                });
        
        jsonObj = JsonObject.loads(response[1].decode());
        return jsonObj;
        
    def getSongUrl2(self):
        response = self.http.request(
            uri='http://music.163.com/weapi/song/enhance/player/url?csrf_token=', 
            method='POST',
            body= urlencode(encrypted_request({
                "ids": [self.obj['id']],
                "br": 160000,
#                 "csrf_token": "e6ad95f1b5d9524aa0da3a9eebbe171f"
                })),
            headers={
#                 'Accept':'*/*',
#                 'Accept-Encoding':'gzip, deflate',
#                 'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
#                 'Cache-Control':'no-cache',
#                 'Connection':'keep-alive',
#                 'Content-Length':'440',
#                 'Host':'music.163.com',
                'Content-Type':'application/x-www-form-urlencoded;',
#                 'Cookie':'_ntes_nnid=e490b3dab908164a2a9e3da85b27de4c,1452134112987; _ntes_nuid=e490b3dab908164a2a9e3da85b27de4c; usertrack=c+5+hVaOIIloZXxKDi8LAg==; __gads=ID=44e5d38bd261f8a3:T=1452563447:S=ALNI_MaBU9gH5m4TVafSwue1AMK1G2g0cg; vjuids=10d453fcd.15233873fee.0.eed88207; vjlast=1452563448.1473665901.22; vinfo_n_f_l_n3=bdd283d69100f4e9.1.9.1452563447906.1465126413756.1473665954669; P_INFO=lian00jian@163.com|1475127175|0|other|11&14|not_found&1474969386&bbs#zhj&330300#10#0#0|135766&0|mail163&bbs|lian00jian@163.com; Province=0571; City=09491; jsessionid-cpta=i5i2drrtLM8CueVXTbjW5i9otEfZSHMc5DrWwiGt6GpiMkOab8NN%5C6MfFAknSnb9pGJ38RGIRy9LFnxjqI9wlti34VZomnE2398Oi7anGhZpO3fznOMNcQfNOZy4km2lCZ5aWS8pUROqJZGwXdjn1%2FgcfHrNEbIpc7YmT45SpU9HT%5CJf%3A1475218594440; c98xpt_=30; __csrf=e6ad95f1b5d9524aa0da3a9eebbe171f; _ga=GA1.2.56167873.1452134116; playerid=80851771; JSESSIONID-WYYY=e0f336e4b8441f31882e4f9dfe2338b64238255f0083abf8b1789be726e9ecf72d37c82116cd7383318ed1948623c9f71620475fcc44b1fbc427ef8247d2d5a6887950a57b06a2bb44bd5a30c76a16127c01f25f299af99372700fac2d4b2140fb6f5c09a25e25f6b00291d4f15d1cc3141778a6d4dea4b4f420dbc5553175086fa1d186%3A1475551764766; _iuqxldmzr_=25; __utma=94650624.56167873.1452134116.1475545392.1475550117.6; __utmb=94650624.2.10.1475550117; __utmc=94650624; __utmz=94650624.1475550117.6.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
#                 'Referer':'http://music.163.com/',
#                 'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
                });
        jsonObj = JsonObject.loads(response[1].decode());
        return jsonObj['data'][0];
        
if __name__ == '__main__':
    songUrlGetter = SongUrlGetter({'id':'280098'});
    print(songUrlGetter.getSongUrl2());