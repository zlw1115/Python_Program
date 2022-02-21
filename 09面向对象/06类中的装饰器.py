# coding:utf-8
'''
classmethod功能
    将类函数可以不经过实例化而直接被调用

用法：
    @classmethod
    def func(cls,...):
        do
参数介绍：
    cls替代普通类函数中的self，变为cls，代表当前操作的是类
'''
class Test(object):
    def __init__(self,a):
        self.a = a

    def run(self):
        print('run')
        self.jump()
        self.sleep()

    @classmethod
    def jump(cls):
        print('jump')
        # cls.run()

    @staticmethod
    def sleep():
        # self.jump()
        print('i want sleep')

t = Test('zlw')
t.run()
# Test.run()
Test.jump()

'''
staticmethod的功能
    将类函数可以不经过实例化而直接被调用，被改装饰器调用的函数不许传递self或cls参数，
    且无法在该函数内调用其它类函数或类变量

用法：
    @staticmethod
    def func(...):
        do
参数介绍：
    函数体内无cls或self参数
    
'''
print('---')
Test.sleep()
t.sleep()
t.jump()
t.run()

'''
property功能：
    将类函数的执行免去括弧，类似于调用属性（变量）
用法：
    @property
    def func(self):
        do
参数介绍：
    无重要函数说明

'''
class Test1(object):
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

test = Test1(name = 'xiaoming')
print(test.name)
test.name = 'zlw'
print(test.name)
