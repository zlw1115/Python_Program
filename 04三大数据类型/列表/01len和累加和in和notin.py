# coding:utf-8
'''
len在列表与元组上的使用
    len函数可以计算出除了数字类型以外，其他所有数据类型的长度

列表（元组）之间的累加与乘法

in和not in在列表（元组）中的用法
    in判断某个成员（元素）是否在该数据结构中
    not in判断某个成员（元素）是否不在该数据结构中
'''
names = ('zenliwen','xiaoming','xiaozhang')
names_add = names + names
names_c = names_add * 10

print(names_add)
print(names_c)

names += ('abc',)
print(names)
names *= 10
print(names)

names_list = ['zengliwen', 'xiaoming']
names_list += ['xiaozeng']
print(names_list)
names_list *= 5
print(names_list)

print('zengliwen' in names_list)
print('zengliwen' not in names_list)