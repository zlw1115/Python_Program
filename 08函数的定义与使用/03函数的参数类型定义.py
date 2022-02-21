# coding:utf-8
'''
参数定义类型的方法
参数+冒号+l类型函数
函数+等号+默认值
def person(name:str,age:int=33):
    print(name,age)

函数定义在python3.7之后可用
函数不会在对参数类型进行验证（业务处理时不符会报错）
'''
def add(a:int, b:int=3):
    print(a+b)
add(1,2)
add('hello','zlw')

def test(a:int,b:int=2,*args:int,**kwargs:str):
    print(a,'-',b,'-',args,'-',kwargs)

test(1,1.2,3,'4',name='zlw')

def test2(a:int,b,c=3):
    print(a,b,c)
test2(1,3,4)