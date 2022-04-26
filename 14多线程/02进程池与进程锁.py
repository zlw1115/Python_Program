# conding:utf-8
'''
进程池的创建---multiprocessing

函数名     介绍          参数              返回值
Pool      进程池创建     Processcount       进程池对象
--
apply-async 任务加入进程池（异步） func,args   无
close       关闭进程池           无           无
join        等待进程池任务结束     无           无
'''
import os
import time
import multiprocessing


def work(count,lock):
    lock.acquire()
    print(count,os.getpid())
    time.sleep(5)
    lock.release()
    return 'result is %s,pid is %s' % (count,os.getpid())


if __name__ == '__main__':
    pool = multiprocessing.Pool(5)
    manager = multiprocessing.Manager()
    lock =manager.Lock()
    results = []
    for i in range(20):
        result = pool.apply_async(func=work,args=(i,lock))
        results.append(result)

    for res in results:
        print(res.get())

    pool.close()
    pool.join()

'''
进程锁
from multiprocessing import Manager
manager = Manager()
lock = manager.Lock()
    
函数名         介绍      参数      返回值
acquire       上锁       无       无
release      开锁（解锁）  无       无
'''
