# coding:utf-8
'''
正则表达式模块 - re
规则
字符串

正则表达式中的特殊字符
特殊字符          描述
\d              匹配任何十进制数字，与[0-9]一致
\D              匹配任意非数字
\w              匹配任何字母数字下划线字符
\W              匹配非字母数字下划线
\s              匹配任何空格字符，与[\n\t\r\v\f]相同
\S              匹配任意非空字符
\A              匹配字符串的起始
\Z              匹配字符串的结束
.               匹配任何字符（除了\n之外）
'''
import re

def had_number(data):
    result = re.findall('\d',data)
    for i in result:
        return True
    return False

def remove_number(data):
    result = re.findall('\D',data)
    print(result)
    return ''.join(result)

def startswith(sub,data):
    _sub = '\A%s' % sub
    result = re.findall(_sub,data)
    for i in result:
        return True
    return False

def endswith(sub,data):
    _sub = '%s\Z' % sub
    result = re.findall(_sub,data)
    if len(result) == 0:
        return False
    return True

def real_len(data):
    result = re.findall('\S',data)
    return len(result)

if __name__ == '__main__':
        data = 'i am zlw,i am 23'
        print(had_number(data))
        result = remove_number(data)
        print(result)
        data = 'hello xiaomu,i am zlw,i am 23 year\'s old'
        print(re.findall('\W',data))
        result = startswith('hellos',data)
        print(result)
        result = endswith('olds',data)
        print(result)
        print(len(data))
        print(real_len(data))