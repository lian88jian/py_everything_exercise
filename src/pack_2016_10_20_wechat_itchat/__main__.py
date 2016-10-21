#!python3
import itchat
from src.pack_2016_10_20_wechat_itchat.tuling import get_response
import threading
import json
from MySQLdb.converters import NoneType
import PyInstaller
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
    
    if msgContent.lower() == dog_name + ' away':
        friend['away'] = True;
        reply = '~~呜~~...╥﹏╥...输入%s come重新召唤' % dog_name;
    elif msgContent.lower() == dog_name + ' come':
        friend['away'] = False;
        reply = '作为一只怪兽，我的愿望是至少消灭一坨奥特曼!';
    else:
        if 'isFirst' not in friend: #是第一次
            reply = "(ฅ´ω`ฅ)我是贱贱的狗狗 %s,贱贱现在不在,我可以陪你聊会儿!输入%s away我将消失" % (dog_name, dog_name)
            friend['isFirst'] = False;
        else:
            reply = get_response(msgContent)
    print(">> %s: %s" % (dog_name, reply) );
    return "%s: %s" % (dog_name, reply);

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
            dog_name = json.loads(f.read())['dog_name'];
            QR = json.loads(f.read())['QR'];
    except:
        except_users = [] #不用机器人的列表
        dog_name = 'noob';
        QR = -2;
        
    itchat.auto_login(True, enableCmdQR = QR)
    friends = itchat.get_friends(True);
    except_users.append(friends[0]['NickName'])
    threading.Thread(target=itchat.run).start();
