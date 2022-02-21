# coding:utf-8
'''
__str__
作用
    如果过定义了该函数，当print当前实例化对象的时候，会返回该函数的return信息
用法：
    def __str__(self):
        return str_type
参数：
    无
返回值：
    一般返回对于该类的描述信息


__getattr__
作用：
    当调用的属性或者方法不存在时，会返回该方法定义的信息
用法：
    def __getattr__(self,key):
    print(sonmething...)
参数：
    key：调用任意不存在的属性名
返回值：
    可以是任意类型也可以不进行返回
'''


class Test(object):
    def __str__(self):
        return 'this is a test class'

    def __getattr__(self, key):
        return '这个key：{}不存在'.format(key)

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            self.__dict__[key] = value
        print('-',self.__dict__)

    def __call__(self,a):
        print('call will start')
        print(a)

t = Test()
print(t)
print(t.a)

'''
__setattr__
作用：
    拦截当前类中不存在的属性与值
用法：
    def __setattr(self,key,value)
        self.__dict__[key] = value
参数：
    key：当前的属性名
    value：当前的参数对应的值
返回值：
    无
    
__call__的功能
作用：
    本质是将一个类变成一个函数
用法：
    def __call__(self,*args,**kwargs):
        print('call will start')
参数：
    可传任意参数
返回值：
    与函数情况相同可有可无
'''
t.name = 'xiaoming'
print(t.name)
t('zlw')

# t.a.b.c 链式操作
class Test2(object):
    def __init__(self,attr=''):
        self.__attr = attr

    def __call__(self):
        print('key is {}'.format(self.__attr))
    def __getattr__(self, key):
        if self.__attr:
            key = '{}.{}'.format(self.__attr,key)
        else:
            key = key
        print(key)
        return Test2(key)

# t2 = Test2()
# t2.a.b.c
