# coding:utf-8
'''
格式化符号：用于对应各种数据类型的格式化符号---格式化符号

%s --- 格式化字符串，通用类型
%d --- 格式化整型
%f --- 格式化浮点型
%u --- 格式化无符号整型（正整型）
%c --- 格式化字符
'''

print('%c' % 123)
print('%c' % 'a')
# print('%c' % ab)
print('%c' % 999999)

print('%u' % 1)
print('%u' % -1)

print('%f' % 1.2)
print('%f' % 12)
print('%f' % 3.14)

print('%d' % 10)
print('%d' % -10)
print('%d' % 10.12)

print('%s' % 123)
print('%s' % 1.23)
print('%s' % '123')

print('{:d}'.format(1))
print('{:f}'.format(1.2))
# 不支持
# print('{:u}'.format(12))
# print('{:s}'.format('1'))

'''
不常用的格式符
%o --- 格式化无符号八进制
%x --- 格式化无符号十六进制
%e --- 科学计数法格式化浮点数
'''
print('%o' % 8)
print('%x' % 32)
# print('%x' % 3ab)

number = int('3ab', 16)
print(number)
print('%x' % number)

print('%e' % 1.2)