#微信聊天机器人之人工智障
#!coding=utf8

import requests
import itchat

KEY = '9ace6a19e68e47d9bfdb8ba8092f1c51'    #小儿子雪桐
KEY1 = '0f4bfc692cb640d3b4a460c813f56e81'   #大女儿雪轩

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    reply = get_response(msg['Text'])
    return reply or defaultReply

itchat.auto_login(hotReload=True)
itchat.run()
