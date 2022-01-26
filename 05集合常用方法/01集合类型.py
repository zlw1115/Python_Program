# coding:utf-8
'''
集合（set）是一个无序的不重复元素序列
常用来对两个列表进行交并差的处理
集合和列表一样，支持所有数据类型

功能      列表          集合
顺序      有序          无序
内容      可重复         不可重复
功能      用于数据的使用   用于数据的交集并集差集的获取
索引      有索引         无索引
符号      [] [1,2,3]      {} {1,2,3}

集合的创建
通过set函数来创建集合，不能使用{}来创建
a_set = set()           空集合
a_set = set([1,2,3])    传入列表或元组
b_set = {1,2,3}         传入元素
c_set = {}              错误，是字典
'''

a = set()
print(a,type(a))

b = set(['python', 'c', 'flask'])
print(b)

# c = {[1,2,3]} # TypeError: unhashable type: 'list'
# c = {{'a': 'b', 'c': 'd'} # TypeError: unhashable type: 'dict'
c = {(1, 2, 3), 1, '123'}  # 所有不可变的成员
print(c)

d = {}
print(d,type(d))

a_list = ['python','c','python','java']
# 去重
b_set = set(a_list)
print(b_set)  # {'python', 'c', 'java'}