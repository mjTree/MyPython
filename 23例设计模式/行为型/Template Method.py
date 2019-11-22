#coding:utf-8

ingredients = 'spam eggs apple'
line = '-' * 10


# 框架
def iter_elements(getter, action):
    # 迭代项的模板框架
    for element in getter():
        action(element)
        print(line)

def rev_elements(getter, action):
    # 以相反顺序迭代项的模板框架
    for element in getter()[::-1]:
        action(element)
        print(line)


# Getters
def get_list():
    return ingredients.split()

def get_lists():
    return [list(x) for x in ingredients.split()]


# Actions
def print_item(item):
    print(item)

def reverse_item(item):
    print(item[::-1])


# 制作模板
def make_template(skeleton, getter, action):
    # 使用getter和action实例化模板方法
    def template():
        skeleton(getter, action)
    return template


# 创建模板功能
templates = [make_template(s, g, a)
             for g in (get_list, get_lists)
             for a in (print_item, reverse_item)
             for s in (iter_elements, rev_elements)] 


for template in templates:
    template()
