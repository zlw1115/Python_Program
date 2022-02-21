#coding:utf-8
'''
多重继承：可以继承多个基（父）类

将被继承的类放入子类的参数位中，用逗号隔开
从左至右依次继承
'''

class Tool(object):
    def work(self):
        return 'tool work'

    def car(self):
        return 'car will run'

class Food(object):
    def work(self):
        return 'food work'

    def cake(self):
        return 'i like cake'

# 继承父类的子类
class Person(Tool,Food):
    pass

if __name__ == '__main__':
    p = Person()
    p_car = p.car()
    p_cake = p.cake()
    print(p_car)
    print(p_cake)
    p_work = p.work()
    print(p_work)