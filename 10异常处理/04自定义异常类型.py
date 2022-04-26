'''
raise
    将信息以报错的形式抛出
用法：
    raise异常类型（message）
参数：
    message：错误信息
返回值：
    无

'''
def test(num):
    if num==100:
        print('start')
        raise ValueError('num 不能为100')
        print('函数内能执行吗')
    return num

# result = test(100) # 程序从这条语句中断
# print('函数外能执行吗')
# print(result)

# result = test(100)

def test2(num):
    try:
        return test(num)
    except ValueError as e:
        return e
# result = test2(100) #except捕获了异常，程序可以接着往下执行
# print(result) #可以执行

def test3():
    raise '错误了'

# test3() #程序从这中断执行

def test4(name):
    if name == 'zlw':
        raise Exception('zlw is not name')
    return name
# test4('zlw')

'''
自定义异常类
继承基类---Exception
在构造函数中定义错误信息
'''
class NumberLimitError(Exception):
    def __init__(self,message):
        self.message = message

class NameLimitError(Exception):
    def __init__(self,message):
        self.message = message

def test5(name):
    if name == 'zlw':
        raise NameLimitError('zlw is not name')
    return name

def test6(number):
    if number >100:
        raise NumberLimitError('数字不可以大于100')
    return number

print('---')
try:
    test5('zlw')
except NameLimitError as e:
    print(e)

try:
    test6(101)
except NumberLimitError as e:
    print(e)