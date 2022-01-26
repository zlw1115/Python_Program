# coding:utf-8
'''
capitalize:将首字母大写，其他字母小写
用法：newstr = string.capitalize()
参数：函数括弧内什么都不用填写
注意：
只对第一个字母有效
只对字母有效
已经是大写，则无效
'''
name = 'xiao mu'
info = 'hello 小慕'
_info = '小慕 hello'
number_str = '123'

new_name = name.capitalize()
new_info = info.capitalize()
_new_info = _info.capitalize()
new_number_info = number_str.capitalize()

# print(new_name)
# print(new_info)
# print(_new_info)
# print(new_number_info)
#
# print(name)
# print(info)

# =========================

'''
casefold：将字符串全体小写，将更多语种转换成小写
newstr = string.casefold() => 函数括弧内什么都不用填写

lower：将字符串全体小写，将英语字母转换
newstr = string.lower() => 函数括弧内什么都不用填写

注意：
只对字符串中的字母有效
已经是小写，则无效
'''
message_en = "How do you do ? zengliwen"
message_ch = '你好，Zeng Liwen'
message_mix = "你好，Zeng Liwen,今天星期3！"

message_en_lower = message_en.lower()
message_en_casefold = message_en.casefold()

message_ch_lower = message_ch.lower()
message_ch_casefold = message_ch.casefold()

message_mix_lower = message_mix.lower()
message_mix_casefold = message_mix.casefold()

# print(message_en_lower,message_en_casefold)
# print(message_ch_lower,message_ch_casefold)
# print(message_mix_lower,message_mix_casefold)

empty = ''
empty_lower = empty.lower()
empty_casefold = empty.casefold()
# print('-',empty_lower,'-')
# print('-',empty_casefold,'-')

# =================================
'''
upper:将字符串全体大写
用法：big_str = string.upper()
参数：函数括弧内什么都不用填写
注意：
子对字符串中的字母有效
已经是大写的，则无效
'''


# ======================
'''
swapcase：将字符串中的大小写字母进行转换
用法：new_str = string.swapcase()
参数：函数括弧内什么都不用写
注意：
只对字符串中的字母有效
'''

# =========================
'''
zfill：为字符串定义长度，如果不满足，缺少的部分用0填补
用法：newstr = string.zfill(with)
参数：
    with:新字符串希望的宽度
注意：
    与字符串的字符无关
    如果定义的长度小于当前字符串长度，则不发生变化
'''
heart = 'love'
# print('    '+heart)
# print(heart.zfill(10))

#=====================
'''
count：返回当前字符串中某个成员（元素）的个数
用法：inttype = string.count(item)
参数：
    item：查询个数的元素
注意：
    如果查询的成员（元素）不存在，则返回0
'''
info = 'asdkafjsadfdsakjh'
a = info.count('a')
print(a)