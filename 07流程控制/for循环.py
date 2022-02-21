# coding:utf-8
'''
用法：
    for item in iterable:
        print(item)
参数：
    iterable:可循环的数据类型 如列表 元组 字符串 字典
    item:iterable中的每一个元素（成员）
返回值：
    for循环式语句，没有返回值，但在特定情况下有返回值

'''

'''
字典利用items函数进行for循环
用法：
    for key,value in dict.items():
        print(key,value)
参数：
    items无参数
    key：for循环体中获取的字典当前元素的key
    value：for循环体中对应当前key的value
返回值：
    for循环是语句，没有返回值，items返回一个为列表

for key in dict.keys():

for value in dict.values():
'''

'''
range内置函数
返回的是一个一定范围的可迭代对象，元素为整型，但不是列表，无法打印信息，但可循环
用法：
    for item in range(start,stop,step=1):
        print(item)
参数：
    start：开始的数字，类似索引的左边
    stop：结束的数字，类似索引的右边
    step：跳步，类似索引的第三个参数
返回值：
    返回一个可迭代（循环的）以整型为主的对象
'''