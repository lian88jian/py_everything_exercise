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
    
    if msgContent.lower() == dog_name.lower() + ' come':
        friend['away'] = False;
        reply = '(ฅ´ω`ฅ) %s来也! 作为一只怪兽，我的愿望是消灭一坨奥特曼!' % dog_name;
    elif 'away' in friend and friend['away'] == True:
        return "";
    elif msgContent.lower() == dog_name.lower() + ' away':
        friend['away'] = True;
        reply = '~~呜~~...╥﹏╥...输入%s come重新召唤' % dog_name;
    else:
        if 'isFirst' not in friend: #是第一次
            reply = "(ฅ´ω`ฅ)我是%s的狗狗 %s,主人现在不在,我可以陪你聊会儿!输入%s away我将消失" % (master_name, dog_name, dog_name)
        else:
            reply = get_response(msgContent)
    friend['isFirst'] = False;
    print(">> %s: %s" % (dog_name, reply) );
    return "%s: %s" % (dog_name, reply);

friends = None;
except_users = None;
def get_friend(userName):
    for f in friends:
        if f['UserName'] == userName:
            if f['NickName'] in except_users or f['RemarkName'] in except_users:
                return None;
            return f;
    return None;

    
if __name__ == '__main__':
    try:
        with open('config.json') as f: 
            config_json = json.loads(f.read());
            except_users = config_json['except_users'];
            dog_name = config_json['dog_name'];
            QR = config_json['QR'];
            master_name = config_json['master_name'];
        print("load config file success!")
    except:
        except_users = [] #不用机器人的列表
        dog_name = 'noob';
        master_name = '贱贱';
        QR = -2;
        
    itchat.auto_login(True, enableCmdQR = QR)
    friends = itchat.get_friends(True);
    except_users.append(friends[0]['NickName'])
    threading.Thread(target=itchat.run).start();
