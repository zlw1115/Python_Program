# coding:utf-8
'''
keys:获取当前字典中所有的键（key）
用法：
    dict.keys() => 无需传参，返回一个key集合的伪列表(不具备列表的所有功能，无法通过索引获取成员，修改，使用内置函数)

'''
project = {'id':1,'project_name':'ipad','price':2000,'count':21}
print(project)

project_title = project.keys()
print(project_title)
print(type(project_title))

project_title = list(project.keys())
print(project_title)
print(type(project_title))
print(project_title[0])
project_title.append('user')
print(project_title)