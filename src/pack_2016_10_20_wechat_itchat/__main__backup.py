#!python3
import itchat
from src.pack_2016_10_20_wechat_itchat.tuling import get_response
from pip._vendor.distlib.compat import raw_input
import threading
# tuling plugin can be get here:
# https://github.com/littlecodersh/EasierLife/tree/master/Plugins/Tuling

@itchat.msg_register('Text')
def text_reply(msg):
    print(msg)
    if '作者' in msg['Text'] or '主人' in msg['Text']:
        return '你可以在这里了解他：https://github.com/littlecodersh'
    elif '源代码' in msg['Text'] or '获取文件' in msg['Text']:
        itchat.send('@fil@main.py', msg['FromUserName'])
        return '这就是现在机器人后台的代码，是不是很简单呢？'
    elif '获取图片' in msg['Text']:
        itchat.send('@img@applaud.gif', msg['FromUserName']) # there should be a picture
    else:
        return get_response(msg['Text']) or '收到：' + msg['Text']

@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def atta_reply(msg):
    return ({ 'Picture': '图片', 'Recording': '录音',
        'Attachment': '附件', 'Video': '视频', }.get(msg['Type']) +
        '已下载到本地') # download function is: msg['Text'](msg['FileName'])

@itchat.msg_register(['Map', 'Card', 'Note', 'Sharing'])
def mm_reply(msg):
    if msg['Type'] == 'Map':
        return '收到位置分享'
    elif msg['Type'] == 'Sharing':
        return '收到分享' + msg['Text']
    elif msg['Type'] == 'Note':
        return '收到：' + msg['Text']
    elif msg['Type'] == 'Card':
        return '收到好友信息：' + msg['Text']['Alias']

@itchat.msg_register('Text', isGroupChat = True)
def group_reply(msg):
    if msg['isAt']:
        return '@%s\u2005%s' % (msg['ActualNickName'],
            get_response(msg['Text']) or '收到：' + msg['Text'])

@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg('项目主页：github.com/littlecodersh/ItChat\n'
        + '源代码  ：回复源代码\n' + '图片获取：回复获取图片\n'
        + '欢迎Star我的项目关注更新！', msg['RecommendInfo']['UserName'])

itchat.auto_login(True, enableCmdQR = -2)
# itchat.run()
threading.Thread(target=itchat.run).start();
# while True:
#     msg = raw_input('send msg to')
#     itchat.send_msg(msg=msg,toUserName='名字太长容易扭到脚');