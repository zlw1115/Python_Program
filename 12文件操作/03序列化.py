'''
可序列化的数据类型
number
str
list
tuple
** dict
'''
'''
json模块
    参数名        参数       介绍          举例                      返回值
    dumps       obj         对象序列化      json.dumps([1,2])        json字符串
    loads       str         反序列化        json.loads('[1,2]')      原始数据类型
'''
'''
pickle模块
方法名     参数      介绍          举例                   返回值
dumps      obj      对象序列化   pickle.dumps([1,2])     比特
loads     byte      反序列化    pickle.loads('[1,2,3]')  原始数据类型
'''
import json
def read(path):
    with open(path,'r') as f:
        data = f.read()
    return json.loads(data)

def write(path,data):
    with open(path,'w',encoding='utf-8') as f:
        if isinstance(data,dict):
            _data = json.dumps(data)
            f.write(_data)
        else:
            raise TypeError('data is not dict')
    return True

data = {'name':'曾丽文','age':18}
if __name__ == '__main__':
    write('test.json',data)
    data = read('test.json')
    print(data)