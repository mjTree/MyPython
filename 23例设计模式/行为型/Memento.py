#coding:utf-8

import copy


def Memento(obj, deep=False):
    state = (copy.copy, copy.deepcopy)[bool(deep)](obj.__dict__)
    
    def Restore():
        obj.__dict__.clear()
        obj.__dict__.update(state)
    return Restore


class Transaction:
    # A transaction guard
    # This is really just syntactic suggar arount a memento closure
    deep = False
    
    def __init__(self, *targets):
        self.targets = targets
        self.Commit()
    
    def Commit(self):
        self.states = [Memento(target, self.deep) for target in self.targets]
    
    def Rollback(self):
        for st in self.states:
            st()


class transactional(object):
    # 向方法添加事务语义,用@transactional修饰的方法将在异常时回滚到入口状态
    def __init__(self, method):
        self.method = method
    
    def __get__(self, obj, T):
        def transaction(*args, **kwargs):
            state = Memento(obj)
            try:
                return self.method(obj, *args, **kwargs)
            except:
                state()
                raise
        return transaction


class NumObj(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return '<%s: %r>' % (self.__class__.__name__, self.value)
    
    def Increment(self):
        self.value += 1
    
    @transactional
    def DoStuff(self):
        self.value = '1111'    # <- 无效值
        self.Increment()       # <- 失败则回滚


if __name__ == '__main__':
    n = NumObj(-1)
    print(n)
    t = Transaction(n)
    try:
        for i in range(3):
            n.Increment()
            print(n)
        t.Commit()
        print('-- commited')
        for i in range(3):
            n.Increment()
            print(n)
        n.value += 'x'    # 将会失败
        print(n)
    except:
        t.Rollback()
        print('-- 回滚')
    print(n)
    print('-- 现在要做的事 --')
    try:
        n.DoStuff()
    except:
        print('-> 做的事失败了！')
        import traceback
        traceback.print_exc(0)
        pass
    print(n)
