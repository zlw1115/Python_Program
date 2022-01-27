# coding:utf-8
'''
bytes比特类型：二进制的数据流，一种特殊的字符串，字符串前+b标记



'''
a = 'hello zengliwen'
print(a,type(a))

b = b'hello zengliwne'
print(b,type(b))

print(b.capitalize())
print(b.replace(b'zengliwen',b'liwen'))
print(b[3])
print(b[:3])
print(b.find(b'x'))

# dir(变量),将变量含有的内置函数打印出来
print(dir(b))

# c=b'hello 曾丽文'

'''
字符串转bytes的函数---encode功能
将字符串转成比特（bytes）类型
用法：
    string.encode(coding='utf-8',errors='strict')
参数：
    encoding：转换成编码格式，如ascii，gbk，默认为utf-8
    errors：出错时的处理方法，默认strict，直接报错误，也可以选择ignore忽略错误
返回值：
    返回一个比特（bytes）类型
    
bytes转字符串的函数---decode
将比特（bytes）类型转成字符串
用法：
    bytes.decode(encoding='utf-8',errors='strict')
参数：
    encoding：转换成的编码格式，如ascii，gbk，默认为utf-8
    errors：出错时的处理方法，默认strict，直接报错误，也可以选择ignore忽略错误
返回值：
    一个字符串类型
'''

str = 'hello 曾丽文'
byte_data = str.encode('utf-8')
print(byte_data,type(byte_data))
print(byte_data.decode('utf-8'))