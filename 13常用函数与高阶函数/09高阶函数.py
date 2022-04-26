# conding:utf-8
'''
filter
    对可迭代对象根据过滤条件进行过滤
用法：
    filter(func,list)
参数介绍：
    func：对list每个item进行条件过滤的定义
    list:需要过滤的列表

map
    对列表中的每个成员是否满足条件返回对应的True和False
用法：
    map(func,list)
参数介绍：
    func:对list每个item进行条件满足的判断
    list：需要过滤的列表

reduce
    对循环前后两个数据进行累加
用法：
    reduce(func,list)
参数介绍
    func:对数据累加的函数
    list：需要处理的列表
不是内置函数，需要引入
from functools import reduce
'''
from functools import reduce

fruits = ['apple','banana','orange']
result = filter(lambda x:'e' in x,fruits)
print(list(result))
print(fruits)

def filter_func(item):
    if 'e' in item:
        return True
print('---')
filter_result = filter(filter_func,fruits)
print(list(filter_result))

map_result = map(filter_func,fruits)
print(list(map_result))

reduce_result = reduce(lambda x,y:x*y,[1,2,3])
print(reduce_result)