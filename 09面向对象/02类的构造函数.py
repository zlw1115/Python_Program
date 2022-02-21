# coding:utf-8
'''
类的构造函数：
    类中的一种默认函数，用来将类实例化的同时，将参数传入类中

def __init__(self,a,b):
    self.a = a
    self.b = b

'''

class Person(object):
    def __init__(self,name,age=None):
        self.name = name
        self.age = age

    def run(self):
        print(f'{self.name} 在奔跑')

    def jump(self):
        print(f'{self.name} 在跳跃')

xiaoming = Person(name='小明',age=10)
xiaoming.name = 'xiaoming'
xiaoming.jump()

