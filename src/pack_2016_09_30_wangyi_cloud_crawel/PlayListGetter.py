'''
Created on 2016年9月30日

@author: lianjian
'''
import httplib2
from pyquery.pyquery import PyQuery

class PlayListGetter:

    def __init__(self, playlistId, cookie):
        self.playlistId = playlistId;
        self.cookie = cookie;
        

    def getSonglist(self):
        http = httplib2.Http();
        response = http.request(uri="http://music.163.com/playlist?id=" + self.playlistId, 
                     method="GET", 
                     #body, 
                     headers={
                         "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                         "Accept-Encoding":"gzip, deflate, sdch",
                         "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
                         "Cookie":self.cookie,
                         "Host":"music.163.com",
                         "Referer":"http://music.163.com/",
                         "Upgrade-Insecure-Requests":"1",
                         "User-Agent":"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36",
                         });
        
        html = response[1].decode();
        jq = PyQuery(html);
        
        songList = [];
        
        jq('ul[class=f-hide] a').each( 
            lambda i, element: 
                songList.append({
                    "id":PyQuery(element).attr('href')[9:],
                    "name":PyQuery(element).text(),
                    "href":PyQuery(element).attr('href')
                    })
            );
        
        return songList;