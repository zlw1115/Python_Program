'''
无论是否发生异常，一定会执行的代码块
在函数中，即便在try或except中进行了return也依然会执行finally语法
try语法至少要伴随except或finally中的一个

用法：
try:
    <代码块1>
except：
    <代码块2>
finally：
    <代码块3>
'''
def test1():
    try:
        1/0
    except ZeroDivisionError as e:
        print(e)
    finally:
        return 'finally'

result = test1()
# print(result)

def test2():
    try:
        1/0
    except ZeroDivisionError as e:
        print('111')
        print(e)
    finally:
        print('finally')
print('----')
test2()

def test3():
    try:
        print('333')
        return 'try'
    except Exception as e:
        print(e)
    finally:
        print('finally test')
print('====')
result = test3()
print(result)

def test4():
    try:
        1/0
    except ZeroDivisionError as e:
        print('1')
        return e
    finally:
        print('2')
        return 'finally'
print('++')
result = test4()
print(result)


def test5():
    try:
        return 'try'
    except ZeroDivisionError as e:
        print(e)
    finally:
        return 'finally'

print('---')
result = test5()
print(result)

def test6():
    try:
        print('try1')
        1/0
        print('try2')
    finally:
        # print('i am finally')
        return 'i am finally'
result = test6()
print(result)