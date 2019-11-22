#coding:utf-8

import time
import random


class TC:
    def __init__(self):
        self._tm = tm
        self._bProblem = 0
    
    def setup(self):
        print('设置测试')
        time.sleep(1)
        self._tm.prepareReporting()
    
    def execute(self):
        if not self._bProblem:
            print('执行测试')
            time.sleep(1)
        else:
            print('设置问题.测试未执行')
    
    def tearDown(self):
        if not self._bProblem:
            print('拆除')
            time.sleep(1)
            self._tm.publishReport()
        else:
            print('测试未执行.不需要拆卸')
    
    def setTM(self, TM):
        self._tm = tm
    
    def setProblem(self, value):
        self._bProblem = value


class Reporter:
    def __init__(self):
        self._tm = None
    
    def prepare(self):
        print('记者班正准备报告结果')
        time.sleep(1)
    
    def report(self):
        print('报告测试结果')
        time.sleep(1)
    
    def setTM(self, TM):
        self._tm = tm


class DB:
    def __init__(self):
        self._tm = None
    
    def insert(self):
        print('在数据库中插入执行开始状态')
        time.sleep(1)
        # 以下代码用于模拟从DB到TC的通信
        if random.randrange(1,4) == 3:
            return -1
    
    def update(self):
        print('在数据库中更新测试结果')
        time.sleep(1)
    
    def setTM(self, TM):
        self._tm = tm


class TestManager:
    def __init__(self):
        self._reporter = None
        self._db = None
        self._tc = None
    
    def prepareReporting(self):
        rvalue = self._db.insert()
        if rvalue == -1:
            self._tc.setProblem(1)
            self._reporter.prepare()
    
    def setReporter(self, reporter):
        self._reporter = reporter
    
    def setDB(self, db):
        self._db = db
    
    def publishReport(self):
        self._db.update()
        rvalue = self._reporter.report()
    
    def setTC(self, tc):
        self._tc = tc


if __name__ == '__main__':
    reporter = Reporter()
    db = DB()
    tm = TestManager()
    tm.setReporter(reporter)
    tm.setDB(db)
    reporter.setTM(tm)
    db.setTM(tm)
    # 为了简化采用循环使用相同的测试
    # 实际上它可以是各种独特的测试类及其对象
    while True:
        tc = TC()
        tc.setTM(tm)
        tm.setTC(tc)
        tc.setup()
        tc.execute()
        tc.tearDown()
