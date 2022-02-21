# coding:utf-8
'''
super函数的作用：
    python子类继承父类的方法而使用的关键字，当子类继承父类后，就可以使用父类的方法了
'''

class Parent(object):
    def __init__(self,p):
        print('hello i am parent %s ' % p)

class Child(Parent):
    def __init__(self,c,p):
        # super关键字###使用明确
        super(Child,self).__init__(p)
        # super().__init__(p)
        print('hello i am child %s' % c)
        #     当前类 类的实例 使用父类的方法

if __name__ == '__main__':
    c = Child(c='Child',p='Parent')