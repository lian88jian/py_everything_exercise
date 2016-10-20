#coding=utf8
import sys, os
import requests, json
from pip._vendor.distlib.compat import raw_input

# tuling plugin can be get here:
# https://github.com/littlecodersh/EasierLife/tree/master/Plugins/Tuling

try:
    with open('config.json') as f: key = json.loads(f.read())['key']
except:
    key = '' # if key is '', get_response will return None
    # raise Exception('There is something wrong with the format of you plugin/config/tuling.json')

def get_response(msg, storageClass = None, userName = None, userid = 'ItChat'):
    url = 'http://www.tuling123.com/openapi/api'
    payloads = {
        'key': key,
        'info': msg,
        'userid': userid,
    }
    try:
        r = requests.post(url, data = json.dumps(payloads)).json()
    except:
        return
    if not r['code'] in (100000, 200000, 302000, 308000, 313000, 314000): return
    if r['code'] == 100000: # 文本类
        return '\n'.join([r['text'].replace('<br>','\n')])
    elif r['code'] == 200000: # 链接类
        return '\n'.join([r['text'].replace('<br>','\n'), r['url']])
    elif r['code'] == 302000: # 新闻类
        l = [r['text'].replace('<br>','\n')]
        for n in r['list']: l.append('%s - %s'%(n['article'], n['detailurl']))
        return '\n'.join(l)
    elif r['code'] == 308000: # 菜谱类
        l = [r['text'].replace('<br>','\n')]
        for n in r['list']: l.append('%s - %s'%(n['name'], n['detailurl']))
        return '\n'.join(l)
    elif r['code'] == 313000: # 儿歌类
        return '\n'.join([r['text'].replace('<br>','\n')])
    elif r['code'] == 314000: # 诗词类
        return '\n'.join([r['text'].replace('<br>','\n')])

if __name__ == '__main__':
    while True:
        a = raw_input('>')
        print(get_response(a, 'ItChat'));