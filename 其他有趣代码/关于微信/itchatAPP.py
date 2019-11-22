#coding:utf8

'''
# 节日群发助手
import itchat, time

itchat.auto_login(True)
SINCERE_WISH = u'祝 %s 新年快乐！'

friendList = itchat.get_friends(update=True)[1:]
for friend in friendList:
    try:
        # 群发消息
        #itchat.send(SINCERE_WISH % (friend['RemarkName'] or friend['NickName']))
        # 做测试
        print((SINCERE_WISH % (friend['RemarkName'] or friend['NickName'])))
    except:
        # 备注或者昵称带有表情符号无法识别出错
        pass
    time.sleep(.5)
'''



import os
import time
import pygame
import itchat


PATH = 'D:/CloudMusic/'  #本地歌曲存储位置

HELP_MSG = u'''\
欢迎使用微信音乐
帮助： 显示帮助
歌单： 显示歌单
播放： 播放歌曲
关闭： 关闭歌曲\
'''

HELP_MSG1 = u'''\
输关键字获取帮助
播放：请输入<播放编号>
如：歌单中有"55红昭愿.mp3"
输入：播放55\
'''

def searchSongs():
    path = PATH
    files= os.listdir(path)
    count = 0
    for i in range(len(files)):
        if str(files[i])[-3:] == 'mp3':
            playlist.append(str(count) + files[i])
            count = count + 1


def playMusic(filename):
    file = PATH + filename
    pygame.mixer.init()
    track = pygame.mixer.music.load(file)
    pygame.mixer.music.play()


def showPlaylist():
    if len(playlist) < 20:
        itchat.send(str(playlist[0:]))
    else:
        for i in range(int(len(playlist)/20)+1):
            if 20*(i+1) < len(playlist):
                itchat.send(str(playlist[20*i:20*(i+1)]))
            else:
                itchat.send(str(playlist[20*i:]))


@itchat.msg_register(itchat.content.TEXT)
def music_player(msg):
    if msg['Text'] == u'帮助':
        itchat.send(HELP_MSG1)
    elif msg['Text'] == u'歌单':
        showPlaylist()
    elif msg['Text'][0:2] == u'播放':
        filename = playlist[int(msg['Text'][2:])][len(msg['Text'][2:]):]
        print(msg['Text'],filename)
        playMusic(filename)
    elif msg['Text'] == u'关闭':
        pygame.mixer.music.stop()
    else:
        # 显示主菜单
        itchat.send(HELP_MSG)

playlist = []
searchSongs()
itchat.auto_login(True)
itchat.send(HELP_MSG) 
itchat.run()


'''
import os  
path = "D:/Python36/WorkSpace/MyPyhton/关于微信"
files= os.listdir(path)
for file in files:
    print(file)
'''


'''
import os
os.system('红昭愿.mp3')
'''




