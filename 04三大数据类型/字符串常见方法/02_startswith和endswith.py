# coding:utf-8
'''
startswith：判断字符串开始是否是某成员（元素）
用法：string.startswith(item)=>item：你想查询匹配的元素，返回一个布尔值


endswith：判断字符串结尾是否是某成员（元素）
用法：string.endswith(item)=>item：你想查询匹配的元素，返回一个布尔值
'''
info = 'this is a string example'
result = info.startswith('this')
print(result)

result = info.startswith('this is a string example')
print(result)
print(bool(info == 'this is a string example'))

result = info.endswith('example')
print(result)
result = info.endswith('this is a string example')
print(result)