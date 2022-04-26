# coding:utf-8
'''
函数名         参数              介绍                  返回值     举例
abs         Number          返回数字绝对值             正数字     abs(-10)
all         List            判断列表内容是否全是true    Bool    all(['','123'])
help        object          打印对象的用法             无     help(list)
enumerate   iterable        迭代时记录索引              无      for index,item enumerate(list)
input       Str             命令行输入消息             Str      input('请输入消息')
isinstance  Object,type     判断对象是否是某种类型       Bool   isinstance('as',str)
type        Object          判断对象类型               Str       type('as')
vars        instance        返回实例化的字典信息         dict
dir         object          返回对象中所有可用方法和属性   List       dir('as')
hasattr     Obj,key         判断对象中是否有某个属性      Bool        hasattr('1','upper')
setattr     Obj,key,value   为实例化对象添加属性与值      无
getattr     obj,key         通过对象获取属性           任何类型        getattr(obj,key)
any         Iterable        判断内容是否又true值        Bool        any['a','',[],1]
'''
# food = input('你想吃什么呢：')
# print(food)
#
# help(input)

class Test(object):
    a = 1
    b = 2

    def __init__(self):
        self.a = self.a
        self.b = self.b


test = Test()
print(test.a)
result = vars(test)
print(result)

print(hasattr(test, 'a'))
print(hasattr(list, 'appends'))

setattr(test, 'c', 3)
print(test.c)
print(vars(test))

# setattr(list, 'c', 1)
if hasattr(list, 'appends'):
    print(getattr(list, 'appends'))
else:
    print('不能存在')

a = ['', None, True, 0]
print(all(a))
print(any(a))
# all - > and
# any - > or