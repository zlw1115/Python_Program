# coding:utf-8
'''
reverse:将当前列表顺序进行反转
用法：list.reverse()
参数：无参数传递

'''
students = [
    {'name':'zengliwen',
     'age':23,
     'top':167
     },
    {
    'name':'ww',
     'age':12,
     'top':177
    },
    {
    'name':'ll',
     'age':27,
     'top':187
    },
    {
    'name':'hh',
     'age':25,
     'top':188
    }
]
print(students)
students.reverse()
print(students)