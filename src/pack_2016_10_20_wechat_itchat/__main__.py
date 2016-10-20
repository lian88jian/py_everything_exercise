#!python3
import itchat
from src.pack_2016_10_20_wechat_itchat.tuling import get_response
from pip._vendor.distlib.compat import raw_input
import threading
from src.pack_2016_10_20_wechat_itchat.sth_fun import check_string_contain
# tuling plugin can be get here:
# https://github.com/littlecodersh/EasierLife/tree/master/Plugins/Tuling


@itchat.msg_register('Text')
def text_reply(msg):
    for f in friends:
        if f['UserName'] == msg['FromUserName']:
            fromFriend = f;
    print('<< %s : %s' % (fromFriend['NickName'] or fromFriend['Signature'], msg['Text'])) 
    reply = ">> robot 66: " + get_response(msg['Text'])
    print(reply) 
    return reply;

friends = None;


def getFriend(userSimpleSpell):
    for f in friends:
        if f['RemarkPYQuanPin'] == userSimpleSpell:
            return f;
    for f in friends:
        if userSimpleSpell in f['RemarkPYQuanPin']:
            return f;
    for f in friends:
        if check_string_contain(f['RemarkPYQuanPin'],userSimpleSpell): 
            return f;
    for f in friends:
        if f['PYQuanPin'] == userSimpleSpell:
            return f;
    for f in friends:
        if userSimpleSpell in f['PYQuanPin']:
            return f;
    for f in friends:
        if check_string_contain(f['PYQuanPin'],userSimpleSpell): 
            return f;
    return None;

if __name__ == '__main__':
    itchat.auto_login(True, enableCmdQR = -2)
    threading.Thread(target=itchat.run).start();
    while True:
        friends = itchat.get_friends();
        print('-------------------------------------------------------------------')
        simpleName = raw_input('** Type the name that you want to send the msg to >> ') #输入好友简拼
        friend = getFriend(simpleName); #获取好友信息
        if friend == None:
            print('** cannot find a friend name contain the words : %s' % simpleName);
            continue;
        flag = raw_input('** Are you sure send msg to %s(%s), Y/N? >> ' % (friend['NickName'], friend['RemarkName'])) #确认好友信息
        if flag.lower() != 'y':
            continue;
        msg = raw_input('** Type the msg content (exit) >> ')
        if msg == 'exit':
            continue;
        itchat.send_msg(msg=msg, toUserName=friend['UserName']);