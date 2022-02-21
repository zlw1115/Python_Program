# coding:utf-8
'''
私有函数和私有对象
    无法被实例化后的对象调用的类中的函数与变量
    类内部可以调用私有函数与变量
    只希望类内部业务调用使用，不希望被使用者调用

私有函数与私有变量的定义方法：
    在变量或函数前添加__(2个下横线)，变量或函数名后边无需添加

'''

class Cat(object):
    __cat_type = 'cat'
    def __init__(self,name,sex):
        self.name = name
        self.__sex = sex

    def run(self):
        result = self.__run()
        print(result)

    def __run(self):
        return f'{self.__cat_type},小猫{self.name}{self.__sex} 开心的奔跑着'

    def jump(self):
        result = self.__jump()
        print(result)

    def __jump(self):
        return f'{self.__cat_type}小猫{self.name}{self.__sex}开心的跳着'

cat = Cat(name='zlw',sex='girl')
cat.run()
cat.jump()
# cat.__run()
print(dir(cat))
print(cat._Cat__jump())
# print(cat.__sex)
print(cat._Cat__sex)