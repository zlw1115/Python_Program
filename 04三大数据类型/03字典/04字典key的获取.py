# coding:utf-8
'''
[]的获取方法
字典+中括号内传key，不进行赋值操作，即为获取
返回key对应的value值

字典内置函数get获取方法
获取当前字典中指定key对应的value值
用法：
    dict.get(key,default=None)
参数：
    key：需要获取value的key
    default：key不存在则返回此默认值，默认是None，也可以自定义

[]和get的区别
    []如果获取的key不存在，则直接报错
    get如果获取的key不存在，则返回默认值
    优先使用get函数
'''
user_info = {
    'id': 1,
    'username': 'zengliwen',
    'passwd': 'abcdefg',
    'created_time': None
}
values = []
values.append(user_info['id'])
values.append(user_info['username'])
values.append(user_info['passwd'])
# values.append(user_info['created_time'])
values.append(user_info.get('created_time','2020-01-02'))
print(values)

# values.append(user_info['birthday'])
values.append(user_info.get('birthday','2020-01-01'))
print(values)