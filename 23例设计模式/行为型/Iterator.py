#coding:utf-8


def count_to(count):
    # 按字数计数,最多五个
    numbers = ['one', 'two', 'three', 'four', 'five']
    # enumerate函数返回一个包含计数的元组(从start开始 默认为0)和迭代序列获得的值
    for pos, number in zip(range(count), numbers):
        yield number


# Test the generator
count_to_two = lambda:count_to(2)
count_to_five = lambda:count_to(5)

print('数二个...')
for number in count_to_two():
    print(number)
print(' ')

print('数五个...')
for number in count_to_five():
    print(number)
print(' ')






