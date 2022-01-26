# coding:utf-8
'''
转义字符：字符要转成其他含义的功能，所以我们叫他转义字符
\ + 字符

\n      换行，一般用于末尾，strip对其也有效
\t      横向制表符（可以认为是一个间隔符）
\v      纵向制表符（会有一个男性符号）
\a      响铃
\b      退格符，将光标前移，覆盖（删除前一个）
\r      回车
\f      翻页（几乎用不到，会出现一个女性符号）
\'      转义字符串中的单引号
\"      转义字符串中的双引号
\\      转移斜杠
'''

'''
转义无效符
在字符串前面加r来字符串中的转移字符无效化
'''
print(r'my name is \\ dawei\n')
print(r'my name is %s' % 'zengliwen')