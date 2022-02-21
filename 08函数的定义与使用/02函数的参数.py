'''
必传参数：
    函数中定义的参数没有默认值，在调用函数时如果不传如则报错
    在定义函数的时候，参数后边没有等号与默认值
def add(a,b)
在定义函数的时候，没有默认值且必须在函数执行的时候传递进去的参数，且顺序与参数顺序相同，就是必传参数

默认参数：
    在定义函数的时候，定义的参数含有默认值，通过赋值语句给他是一个默认的值
    def add(a,b=1)
              参数名，复制等号，默认值
如果默认参数在调用函数的时候给与了新的值，函数将优先使用后传入的值进行工作

不确定参数--可变参数:
    没有固定的参数名和数量（不知道要传的参数名具体是什么）
    def add(*args,**kwargs):
        add(1,2,3,name='zlw',age=23)
            1,2,3:对应*args
            name='zlw',age=23:对应**kwargs
*args代表：将无参数的值合并成元组
**kwargs代表：将有参数与默认值的赋值语句合并成字典
'''

def test(a, b=1, *args):
    print(a, b, args)

s = (1, 2)
test(1, 2, *s)
# test(a=1, b=2, *s) # TypeError: test() got multiple values for argument 'a'

def test2(*args, a, b=1):
    print(a, b, args)
test2(a=1, b=2, *s)

def test3(a, b=1, **kwargs):
    print(a, b, kwargs)

test3(1, 2, name='zlw')
test3(a=1, b=2, name='zlw')
test3(name='zlw', age=23, a=1, b=2)

d = {'name':'zlw'}
test3(a=1, b=2, **d)
test3(**d, a=1, b=2)
# test3(**d, 1, 2)