# coding:utf-8
'''
异常的语法
try:
    <代码块1>被try关键字检查并保护的业务代码
except <异常类型>：
    <代码块2> # 代码块1出现错误后执行的代码块

'''
def upper(str_data):
    new_str = 'None'
    try:
        new_str = str_data.upper()
    except Exception as e:
        print('程序出错了:{}'.format(e))
    # print语句还可以执行
    print('aa')
    return new_str

def test():
    try:
        print('123')
        1/0
        print('hello')
    except ZeroDivisionError as e:
        print(e)

# result = upper(1) #捕获到了异常
# test() # 继续执行了这条语句，捕获到了异常
# print('执行了吗') # 继续执行了这条语句

'''
捕获通用异常类型
    无法确定是哪种异常的情况下使用的捕获方法
    try:
        <代码块>
    except EXception as e:
        <异常代码块>
        
捕获具体异常
    确定是那种异常的情况下使用的异常方法
    except <具体的异常类型> as e
    
'''

'''
捕获多个异常
try:
    print('try start')
    res = 1/0
    print('try finish')
except ZeroDivisionError as e:
    print(e)
except Exception as e:# 可以有多个except
    print('..')
    
当except代码块有多个的时候，当捕获到第一个后不会继续往下捕获

第二种
try:
    print('try start')
    res = 1/0
    print('try finish')
except (ZeroDivisionError,Exception) as e:
    print(e)
当except代码后边的异常类型使用元组包裹起来，捕获到那种抛那种
'''
def test1():
    try:
        print('try start')
        res = 1 / 0
        print('try finish') # 这条语句不执行
    except Exception as e:
        print('Exception')
        print(e)
    except ZeroDivisionError as e:  # 可以有多个except
        print('ZeroDivisionError')
        print(e)

test1()