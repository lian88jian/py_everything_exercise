#!python3
import itchat
from src.pack_2016_10_20_wechat_itchat.tuling import get_response
import threading
import json
from MySQLdb.converters import NoneType
# tuling plugin can be get here:
# https://github.com/littlecodersh/EasierLife/tree/master/Plugins/Tuling

@itchat.msg_register('Text')
def text_reply(msg):
    friend = get_friend(msg['FromUserName'])
    if friend == None: 
        return "";
    fromUserName = friend['RemarkName'] or friend['NickName'] or friend['Signature'];
    msgContent = msg['Text'];
    
    print('<< %s : %s' % (fromUserName, msgContent)) 
    
    if msgContent.lower() == 'qq away':
        friend['away'] = True;
        reply = '~~呜~~...╥﹏╥...输入dog come重新召唤';
    elif msgContent.lower() == 'qq come':
        friend['away'] = False;
        reply = '作为一只怪兽，我的愿望是至少消灭一坨奥特曼!';
    else:
        if 'isFirst' not in friend: #是第一次
            reply = "(ฅ´ω`ฅ)我是贱贱的狗狗 QQ,贱贱现在不在,我可以陪你聊会儿!输入QQ away我将消失"
            friend['isFirst'] = False;
        else:
            reply = get_response(msgContent)
    print(">> QQ: " + reply);
    return "QQ: " + reply;

friends = None;
except_users = None;
def get_friend(userName):
    for f in friends:
        if f['UserName'] == userName:
            f['away'] = False;
            if f['NickName'] in except_users:
                return None;
            return f;
    return None;

    
if __name__ == '__main__':
    try:
        with open('config.json') as f: 
            except_users = json.loads(f.read())['except_users']
    except:
        except_users = [] #不用机器人的列表
        
    itchat.auto_login(True, enableCmdQR = -2)
    friends = itchat.get_friends(True);
    except_users.append(friends[0]['NickName'])
    threading.Thread(target=itchat.run).start();
