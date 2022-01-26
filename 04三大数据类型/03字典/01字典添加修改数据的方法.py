# coding:utf-8
'''
[]处理法
字典没有索引
dict['name']='zlw'
添加或修改，根据key是否存在决定

字典的内置函数 update
添加新的字典，如新字典中有和原字典相同的key，则该key的value会被新字典的value覆盖
用法：
    dict.update(new_dict) => 该函数无返回值
参数：
    new_dict:新字典

字典的内置函数 setdefault
获取某个key的value，如果key不存在于字典中，将会添加key并将value设置为默认值
用法：
    dict.setdefault(key,value)
参数：
    key需要获取的key
    value如果key不存在，对应这个key存入字典的默认值

字典注意事项：
    字典中每一个key一定是唯一的
    字典中的数据量没有限制
    字典中的value可以是任何python的内置数据类型的对象和自定义对象
'''
user = {'username': 'zlw', 'age': 23}

# user['top'] = 1.67
# print(user)
#
# user['username'] = 'hh'
# print(user)
# user['top'] = 175
# user['age'] = 31
# print(user)

xiaoming = {'username': '小明', 'age':12, 'top': 1.56,'sex': "男"}
user.update(xiaoming)
# print(user)


value = user.setdefault('username', 'xiaoyun')
print(user,value)
value = user.setdefault('birthday', '2022-1-23')
print(user,value)