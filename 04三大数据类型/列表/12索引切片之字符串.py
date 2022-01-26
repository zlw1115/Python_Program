# coding:utf-8
'''
字符串的索引、获取
字符串的finde，index函数
字符串索引规则与列表相同
字符串切片和索引的获取与列表相同
字符串无法通过索引修改与删除
字符串不可修改
'''
'''
find index
功能：获取元素的索引位置
用法：
    string.index(item)=>item:查询个数的元素，返回索引位置
    string.find(item)=>item:查询个数的元素，返回索引位置
区别：
    find如果获取不到，返回-1
    index如果获取不到，直接报错

'''
# 字符串反序
name = 'zengliwen'
temp = []
# temp.append(name[0])
# temp.append(name[1])
# temp.append(name[2])
# temp.append(name[3])
# temp.append(name[4])
# temp.append(name[5])
# temp.append(name[6])
# temp.append(name[7])
# temp.append(name[8])
# temp.extend(name)
# print(temp)
# temp.reverse()
# print(temp)
# new_name = '%s%s%s%s%s%s%s%s%s' % (temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8])
# print(new_name)
new_name = name[::-1]
print(new_name)

result = new_name.find('ew')
print(result)
result =new_name.index('ew')
print(result)

result = new_name.find('we')
print(result)
result =new_name.index('we') # ValueError: substring not found
print(result)