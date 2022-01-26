#coding:utf-8

'''
内置成员运算符in的使用
 - 成员运算符是用来判断你的数据中是否存在你想要的成员

 内置函数max
 - max函数返回数据中最大的成员
 max(数据) -> 成员值 print(max('今天是1月3日！'))? 月
 中文符号 > 字母 > 数字 > 英文符号
 中文按照拼英的首字母来计算

 内置函数min
  - min函数返回数据中的最小数据
'''
'''
字符串的累加
- 字符串不是数字不能做减法，乘除法
- 字符串拼接，用'+'这个符号
'''

info = "python是一门非常有魅力的语言"

result = '魅力' in info
print(result)

result = '语言' not in info
print(result)

info2 = 'python is good code'
print(max(info2))
print('.', min(info2), '.')

info3 = '天气好，要多锻炼身体'
info4 = '多锻炼身体，身体更好'
new_str = info3 + info4 + "!"
print(new_str)
print(len(new_str))