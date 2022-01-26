# coding:utf-8
'''
strip:去掉开头或结尾的元素
用法：newstr = string.strip(item)
参数：括弧里需要传一个你想去掉的元素，可不填写，默认为空格
注意：传入的元素如果不在开头或结尾则无效
    lstrip仅去掉字符串开头的指定元素或空格
    rstrip仅去掉字符串结尾的指定元素或空格
'''
info = '   my name is Zeng Liwen '
new_info = info.strip()
print('-'+new_info+'-')

info_01 = 'my name is Zeng Liwen'
new_info_01 = info_01.strip(info_01)
print(new_info_01)
print(len(new_info_01))

new_str = 'abcdea'
print(new_str.strip('a'))
print(new_str.lstrip('a'))
print(new_str.rstrip('a'))
