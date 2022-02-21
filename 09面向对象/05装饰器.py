# coding:utf-8
'''
装饰器：
    也是一种函数
    可以接受函数作为参数
    可以返回函数
    接收一个函数，内部对其处理，然后返回一个新函数，动态的增强函数功能
    将c函数在a函数中执行，在a函数中可以选择执行或不执行c函数，也可以对函数的结果进行二次加工处理
用法：
    将被调用的函数直接作为参数传入装饰器的外围函数括弧
    将装饰器与被调用函数绑定在一起
    @符号+装饰器函数放在被调用函数的上一行，被调用的函数正常定义，只需要直接调用被执行函数即可

'''

def check_str(func):
    print('func:',func)
    def inner(*args, **kwargs):
        print('args:',args,'kwargs:',kwargs)
        result = func(*args, **kwargs)
        if result == 'ok':
            return 'result is %s ' % result
        else:
            return 'result is failed:%s' % result
    return inner

@check_str
def test(data):
    return data

result = test('no')
print(result)

result = test(data = 'yes')
print(result)