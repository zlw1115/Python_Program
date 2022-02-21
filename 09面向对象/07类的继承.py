# coding:utf-8
'''
父类与子类的关系
    子类拥有父类的所有属性和方法
    父类不具备子类自有的属性和方法

定义子类时，将父类传入子类参数内
子类实例化后可以调用自己与父类的函数与变量
父类无法调用子类的独有函数与变量
'''
class Parent(object):
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
    def talk(self):
        return f'{self.name} are talking'

    def is_sex(self):
        if self.sex == 'boy':
            return f'{self.name} is boy'
        else:
            return f'{self.name} is girl'

class ChildOne(Parent):
    def play_football(self):
        return f'{self.name} are playing football'

class ChildTwo(Parent):
    def play_pingpong(self):
        return f'{self.name} are playing pingpong'

c_one = ChildOne(name='xiaoming',sex='boy')
result = c_one.play_football()
print(result)
print(c_one.talk())

c_two = ChildTwo(name='zlw',sex='girl')
result = c_two.play_pingpong()
print(result)
print(c_two.sex)

p = Parent(name='小明爸爸',sex='boy')
print(p.talk())
print(p.play_pingpong())