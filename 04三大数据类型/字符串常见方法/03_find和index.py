# coding:utf-8
'''
find和index都是返回你想寻找的成员的位置

用法：
    string.find(item) => item：你想查询的元素，返回一个整型
    返回-1

    string.index(item) => item：你想查询的元素，返回一个整型
    或者报错
'''
info = 'python is a good code'

result = info.find('is')
print(result)
result = info.find('ok')
print(result)

result = info.index('is')
print(result)
result = info.index('ok')
print(result)