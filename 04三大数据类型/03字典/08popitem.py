# coding:utf-8
'''
popitem 删除当前字典里末尾一组键值对并将其返回

用法：
    dict.popitem() --无需传参
    返回被删除的键值对，用元组包裹0索引是key，1索引是value

注意：如果字典为空，则报错
'''
students = {'zlw':'到','xiaoming':'在','xiaozang':'在呢'}
print('xiaozhang在吗')
xiaozhang = students.popitem()
print('{} 喊 {}'.format(xiaozhang[0],xiaozhang[1]))
xiaoming = students.popitem()
print('{} 喊 {}'.format(xiaoming[0],xiaoming[1]))
zlw = students.popitem()
print('{} 喊 {}'.format(zlw[0],zlw[1]))
print(students)
students.popitem() # KeyError: 'popitem(): dictionary is empty'