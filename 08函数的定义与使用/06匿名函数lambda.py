# coding：utf-8
'''
lambda功能：
    定义一个轻量化的函数
    即用即删除，很适合需要完成一项功能但是此功能只在此一处使用

匿名函数的定义方法
    无参数
    f = lambda : value
    f()
    有参数
    f = lambda x,y : x*y
    f(3,4)
'''
# f = lambda: 1
# result = f()
# print(result)
# f = lambda: return 1
f = lambda: print(1)
f()

# f1 = lambda x,y:x+y
# print(f1(1,2))
f1 = lambda x=1,y=2:x+y
print(f1())