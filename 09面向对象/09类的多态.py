# coding:utf-8
'''
同一个功能的多状态化
多态的用法：
    子类中重写父类的方法

'''
# 1、书写一个父类
class XiaomingFather(object):
    def talk(self):
        print('小明的爸爸说了一句话')

class XiaomingBorther(XiaomingFather):
    def run(self):
        print('小明哥哥奔跑着')
    def talk(self):
        print('小明哥哥在说话')

# 为什么要用多态
# 为什么要去继承父类
# 答案：为了使用已经写好的类中的函数
# 为了保留子类中某个和父类名称一样的函数的功能，这时候，我们就用到了类的多态
# 可以帮助我们保留子类中的函数功能

class Xiaoming(XiaomingFather):
    def talk(self):
        print('小明说话')
if __name__ == '__main__':
    xiaoming_borther = XiaomingBorther()
    xiaoming_borther.talk()
    xiaoming_father = XiaomingFather()
    xiaoming_father.talk()
    xiaoming = Xiaoming()
    xiaoming.talk()