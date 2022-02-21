# coding:utf-8
'''
类的参数self
    self是类函数中必传的参数，且必须放在第一个参数位置
    self是一个对象，他代表实例化的变量自身
    self可以直接通过点来定义一个类变量 self.name = 'zlw'
    self中的变量与含有self参数的函数可以在类的任何一个函数内随意调用
    非函数中定义的变量在定义的时候不用self
'''
class Person(object):
    name = None
    age = None

    def run(self):
        print(f'{self.name} 在奔跑')

    def jump(self):
        print(f'{self.name} 在跳跃')

    # def sleep():
    #     print('sleep')

    def work(self):
        self.run()
        self.jump()
        def sleep(name):
            return name
        result = sleep(self.name)
        print('sleeep result is {}'.format(result))


xiaoming = Person()
xiaoming.name = '小明'
xiaoming.run()
xiaoming.jump()

dewei = Person()
dewei.run()

dewei.top = 1.88
print(dewei.top)
# print(xiaoming.top)

xiaoming.work()
xiaoming.sleep()