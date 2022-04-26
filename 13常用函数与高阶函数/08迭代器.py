# coding:utf-8
'''
iter
    生成一个迭代器对象
用法：
    iter(iterable)
参数介绍：
    iterable：可迭代的数据类型

for循环生成发--yield
for循环一行生成法
    不会报错
'''
iter_obj = iter((1,2,3))

def _next(iter_obj):
    try:
        return next(iter_obj)
    except StopIteration:
        return None

# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))

# print(_next(iter_obj))
# print(_next(iter_obj))
# print(_next(iter_obj))
# print(_next(iter_obj))

for i in iter_obj:
    print(i)

def make_iter():
    for i in range(10):
        yield i

iter_obj = make_iter()
print(type(iter_obj))

for i in iter_obj:
    print(i)
print('----')
for i in iter_obj:
    print(i)


iter_obj = (i for i in range(10))
for i in iter_obj:
    print(i)
print('===')
for i in iter_obj:
    print(i)