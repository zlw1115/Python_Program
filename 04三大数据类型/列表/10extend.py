# coding:utf-8
'''
extend:将其他列表或元组中的元素倒入到当前列表中
用法：list.extend(iterable)->
参数：
    iterable代表列表或元素，该函数无返回值
'''
manhu = []
history = []
code = []

new_manhu = ('a', 'b', 'c')
new_history = ('中国历史', '日本历史', '安国列表')
new_code = ('python', 'c', 'java')
manhu.extend(new_manhu)
history.extend(new_history)
code.extend(new_code)

print(manhu)
print(history)
print(code)

history.extend(manhu)
del manhu
print(history)

test = []
test.extend('abd') # 'a' 'b' 'c'
# test.extend(1) # TypeError: 'int' object is not iterable
# test.extend(None) # TypeError: 'NoneType' object is not iterable
test.extend({"name":"zlw","age":12}) # key值添加进去了
# test.extend(True) #TypeError: 'bool' object is not iterable
print(test)