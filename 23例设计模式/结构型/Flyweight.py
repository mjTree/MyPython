#coding:utf-8

import weakref

class Card(object):
    # 对象池 内建引用计数
    _CardPool = weakref.WeakValueDictionary()
    
    # 轻量级实现.如果对象存在于池中,则返回它(而不是创建一个新对象)
    #'''
    def __new__(cls, value, suit):
        obj = Card._CardPool.get(value + suit, None)
        if not obj:
            obj = object.__new__(cls)
            Card._CardPool[value + suit] = obj
            obj.value, obj.suit = value, suit
        return obj
    
    '''
    def __init__(self,value, suit):
        self.value, self.suit = value, suit
    #'''
    
    def __repr__(self):
        return '<Card: %s%s>' %(self.value, self.suit)


if __name__ == '__main__':
    # 注释__new__函数或__init__函数,查看两个id的结果
    c1 = Card('9', 'h')
    c2 = Card('9', 'h')
    print(c1, c2)
    print(c1 == c2)
    print(id(c1), id(c2))
