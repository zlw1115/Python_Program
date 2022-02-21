# coding:utf-8
'''
字符串转列表的函数---split
以一定规则将字符串切割成列表
用法：
    string.split(sep=None,maxsplit=-1)
参数：
    sep：切割的规则符号，不填写，默认空格，如字符串无空格则不分割成列表
    maxsplit：根据切割符号切割的次数，默认-1无限制
返回值：
    返回一个列表

列表转字符串的函数---join
将列表按照一定规则转成字符串
用法：
    'sep'.join(iterable)
参数：
    sep：生成的字符串用来分割列表每个元素的符号
    iterable：非数字类型的列表或元组或集合
返回值：
    返回一个字符串
'''
a = 'abc'
print(a.split())
b = [1, 2, 3]
# print(''.join(b)) # TypeError: sequence item 0: expected str instance, int found
