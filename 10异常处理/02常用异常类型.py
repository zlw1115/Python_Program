'''
异常名称            说明
Except             通用异常类型（基类）
ZeroDivisionError  不能整除0
AttributeError      对象没有这个属性
IOError             输入输出操作失败
IndexError          没有当前的索引
KeyError            没有这个键值（key）
NameError           没有这个变量（未初始化对象）
SyntaxError         解释器的系统错误
ValueError          传入的参数错误

'''
class Test(object):
    pass
t = Test()
try:
    t.name
except AttributeError as e:
    print(e)

d= {'name':'zlw','age':12}
try:
    d['sex']
except KeyError as e:
    print('没有对应的键',e)