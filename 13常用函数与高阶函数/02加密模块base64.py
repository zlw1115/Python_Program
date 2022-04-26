# coding:utf-8
'''
通用型，可解密
函数名             参数      介绍              举例                              返回值
encodestring       byte     进行base64加密     base64.encodestring(b' py')      byte
decodestring     byte     对base64解密       base64.decodestring(b'eGlhb211\n') byte
以上从python3.1开始被弃用
encodebytes        byte     进行base64加密      base64.encodebytes(b'py')           byte
decodebytes       byte    对base64解密       base64.decodebytes(b'eGlhb211\n') byte
'''
import base64

replace_one = '%'
replace_two = '$'

def encode(data):
    if isinstance(data,str):
        data = data.encode('utf-8')
    elif isinstance(data,bytes):
        data = data
    else:
        raise TypeError('data need bytes or str')
    _data = base64.encodebytes(data).decode('utf-8')
    # _data = base64.encodestring(data).decode('utf-8')
    print(_data)
    _data = _data.replace('a',replace_one).replace('2',replace_two)
    print(_data)
    return _data

def decode(data):
    if not isinstance(data,bytes):
        raise TypeError('data need bytes')
    replace_one_b = replace_one.encode('utf-8')
    replace_two_b = replace_two.encode('utf-8')
    data = data.replace(replace_one_b,b'a').replace(replace_two_b,b'2')
    return base64.decodebytes(data).decode('utf-8')
    # return base64.decodestring(data).decode('utf-8')


if __name__ == '__main__':
    result = encode('hello zlw')
    # print(result)
    new_result = decode(result.encode('utf-8'))
    print(new_result)