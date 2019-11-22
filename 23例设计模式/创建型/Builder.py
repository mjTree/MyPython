#!/usr/bin/python
#coding:utf-8
# Builder.py


# 主管类
class Director(object):
    def __init__(self):
        self.builder = None
    
    def construct_building(self):
        self.builder.new_building()
        self.builder.build_floor()
        self.builder.build_size()
    
    def get_building(self):
        return self.builder.building


# 摘要构建器
class Builder(object):
    def __init__(self):
        self.building = None
    
    def new_building(self):
        self.building = Building()


# 具体建造者
class BuilderHouse(Builder):
    def build_floor(self):
        self.building.floor = 'One'
    
    def build_size(self):
        self.building.size = 'Big'


class BuilderFlat(Builder):
    def build_floor(self):
        self.building.floor = 'More than One'
    
    def build_size(self):
        self.building.size = 'Small'


# 生产
class Building(object):
    def __init__(self):
        self.floor = None
        self.size = None
    
    def __repr__(self):
        return 'Floor: %s | Size: %s' % (self.floor, self.size)


# 用户
if __name__ == '__main__':
    director = Director()
    director.builder = BuilderHouse()
    director.construct_building()
    building = director.get_building()
    print(building)
    director.builder = BuilderFlat()
    director.construct_building()
    buildiing = director.get_building()
    print(buildiing)






