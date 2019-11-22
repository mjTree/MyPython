#coding:utf-8

import time


SLEEP = 0.5

# Complex Parts
class TC1:
    def run(self):
        print('-------- 测试1 --------')
        time.sleep(SLEEP)
        print('开始设置')
        time.sleep(SLEEP)
        print('测试开始')
        time.sleep(SLEEP)
        print('开始拆除')
        time.sleep(SLEEP)
        print('测试结束\n')

class TC2:
    def run(self):
        print('-------- 测试2 --------')
        time.sleep(SLEEP)
        print('开始设置')
        time.sleep(SLEEP)
        print('测试开始')
        time.sleep(SLEEP)
        print('开始拆除')
        time.sleep(SLEEP)
        print('测试结束\n')

class TC3:
    def run(self):
        print('-------- 测试3 --------')
        time.sleep(SLEEP)
        print('开始设置')
        time.sleep(SLEEP)
        print('测试开始')
        time.sleep(SLEEP)
        print('开始拆除')
        time.sleep(SLEEP)
        print('测试结束\n')


# Facade
class TestRunner:
    def __init__(self):
        self.tc1 = TC1()
        self.tc2 = TC2()
        self.tc3 = TC3()
        self.tests = [i for i in (self.tc1, self.tc2, self.tc3)]

    def runAll(self):
        [i.run() for i in self.tests]


# Client
if __name__ == '__main__':
    testrunner = TestRunner()
    testrunner.runAll()

#testrunner.tests[0].run()
