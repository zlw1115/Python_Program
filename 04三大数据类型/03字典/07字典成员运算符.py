# coding:utf-8
'''
in和 not in在字典中的用法

字典内置的get

'''
default_dict = {'a':None,'b':1,'c':0,'d':''}
print('a' in default_dict)
print(bool(default_dict['a']))
print(bool(default_dict.get('a')))
print(bool(default_dict.get('b')))
print('f' in default_dict)
print(default_dict.get('f'))