# conding:utf-8
'''
进程的创建模块--multiprocessing
函数名         介绍          参数               返回值
Process       创建一个进程    target，args      进程对象
---
start         执行进程       无                  无
join          阻塞程序       无                  无
kill          杀死进程       无                  无
is_alive      进程是否存活    无                   bool

'''
import time
import os
import multiprocessing

def work_a():
    for i in range(10):
        print(i,'a',os.getpid())
        time.sleep(1)

def work_b():
    for i in range(10):
        print(i,'b',os.getpid())
        time.sleep(1)

if __name__ == '__main__':
    strat = time.time() # 主进程1
    a_p = multiprocessing.Process(target=work_a) # 子进程1
    # a_p.start() # 子进程1执行
    # a_p.join()
    b_p = multiprocessing.Process(target=work_b) # 子进程2
    # b_p.start() # 子进程2执行
    for p in (a_p,b_p):
        p.start()

    for p in (a_p,b_p): #意义是什么
        p.join()

    for p in (a_p,b_p):
        print(p.is_alive())

    print(time.time()-strat) #主进程代码2
    print('parent pid is %s' % os.getpid())

'''
多进程问题：
    通过进程模块执行的函数无法获取返回值
    多个进程同时修改文件可能会出现错误
    进程数量太多可能会造成资源不足，甚至死机等情况
'''