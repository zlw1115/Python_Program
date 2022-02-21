# coding:utf-8
'''
全局变量
    在python脚本的最上层代码块的变量
    全局变量可以在寒素内被读取使用（不能被修改）
局部变量
    在函数体内定义的变量
    局部变量无法在自身函数以外使用
'''
name = 'zlw'
def test():
    print(name)
test()
def test1():
    name = '曾丽文'
    print('函数体内',name)
test1()
print('函数体外',name)

'''
global
    将全局变量可以在函数体内进行修改
    工作中：不建议使用global对全局变量修改
仅支持：字符串，数字，空类型，布尔类型
列表，字典不需要global进行声明，就可以在函数内修改
'''
def test2():
    global name
    name = 10

test2()
print(name)

test_dict = {'a':1,'b':2}
def test3():
    test_dict['c'] = 3
    test_dict.pop('a')

test3()
print(test_dict)