'''
Created on 2016年9月30日

@author: lianjian
'''
from src.pack_2016_09_30_wangyi_cloud_crawel.SongUrlGetter import SongUrlGetter
from urllib.request import urlretrieve
from pack_2016_09_30_wangyi_cloud_crawel.PlayListGetter import PlayListGetter
import logging
import sys

cookie = "";

if __name__ == '__main__':
    paylistId = sys.argv[1];
    paylistId = sys.argv[2];
    
    playListGetter = PlayListGetter(paylistId,cookie);
    #获取歌单歌曲列表
    songList = playListGetter.getSonglist();
    
    for song in songList:
        songUrlGetter = SongUrlGetter(song);
        #歌曲下载地址
        songUrl = songUrlGetter.getSongUrl2();
        try:
            urlretrieve(songUrl['url'],filename='E:\\temp\\music\\' + song['name'] + '.mp3');
            print('%s download complete' % song['name'])
        except:
#             print('%s,[%s][%s] download fail for: %s' % (song['id'],songUrl['url'],song['name'], e));
            logging.exception('%s,[%s][%s] download fail' % (song['id'],songUrl['url'],song['name']));