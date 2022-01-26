# coding:utf-8
'''
定居类型定义的格式u啊
    字符串格式化使用操作符 % 来实现
    eg:
        'my name is %s,my age is %s' % ('Zeng Liwen',23)
        前两个 % 格式符
        第三个 % :格式化字符串与格式符变量之间用一个 % 链接，%两边有1个空格
        ('Zeng Liwen',23)：对应格式符的变量，变量与格式符按顺序一一对应，数量保持一致，
                          超过1个格式化变量用小括号包裹
'''
info = 'my name is %s, my age is %s' % ('Zengliwen',10)
# print(info)

info = 'my name is %s, my age is %s'
name_01 = '曾丽文'
age_01 = 23

name_02 = '哈哈'
age_02 = 12

# print(info % (name_01, age_01))
# print(info % (name_02, age_02))

'''
字符串格式化函数 - format
string.format 函数用来格式化字符串
使用format的字符串主体使用{}大括号来替代格式符
string.format(data1,data2,...)
'''
info_02 = 'my name is {0}, my age is {1},my book is {2}'
books = ['a', 'b', 'c']
print(info_02.format('曾丽文', 23, books))

'''
python3.6加入的新格式化方案  f-string
    定义一个变量
    字符串前加f符号
    需要格式化的位置使用{变量名}
'''
info_3 = f'my name is {name_01}, my age is {age_01}'
print(info_3)
