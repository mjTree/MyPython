#coding:utf-8

import time


class SalesManager:
    def work(self):
        print('销售经理正在工作')
    
    def talk(self):
        print('销售经理准备好说了')


class Proxy:
    def __init__(self):
        self.busy = 'No'
        self.sales = None
    
    def work(self):
        print('代理检查销售经理的可用性')
        if self.busy == 'No':
            self.sales = SalesManager()
            time.sleep(2)
            self.sales.talk()
        else:
            time.sleep(2)
            print('销售经理很忙')


if __name__ == '__main__':
    p = Proxy()
    p.work()
    p.busy = 'Yes'
    p.work()

