#!/usr/bin/python
#coding:utf-8
# FactoryMethod.py


class ChinaGetter:
    # 一个简单的定位器
    def __init__(self):
        self.trans = dict(dog = u'小狗', cat = u'小猫')
    
    def get(self, msgid):
        # 有异常就抛出
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)


class EnglishGetter:
    # 简单回应msg ids
    def get(self, msgid):
        return str(msgid)


def get_localizer(language = 'English'):
    # 工厂模式
    languages = dict(English = EnglishGetter, China = ChinaGetter)
    return languages[language]()


# 创建本地化器
e, g = get_localizer('English'), get_localizer('China')
# 本地化一些文字
for msgid in 'dog parrot cat bear'.split():
    print(e.get(msgid), g.get(msgid))

