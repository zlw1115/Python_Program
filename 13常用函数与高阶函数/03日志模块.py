'''
日志等级
低-高
debug
info
warnning
error
critical
'''
import os

'''
logging模块
loggin.basicConfig
参数名     作用              举例
level      日志输出等级       level=logging.DEBUG
format      日志输出格式      
filename    存储位置        filename='d://back.log'
filemode    输入模式        filemode='w'

format具体格式
格式符                 含义  
%(levelname)s       日志级别名称
%(pathname)s        执行程序的路径
%(filename)s        执行程序名
%(lineno)d          日志的当前行号
%(asctime)s         打印日志的时间
%(message)s         日志信息

format = '%(asctime)s %(filename)s[line:%lineno)d]%(levelname)s%(message)s'

'''

import logging
import os
def init_log(path):
    if os.path.exists(path):
        mode = 'a'
    else:
        mode = 'w'
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s',
        filename=path,
        filemode=mode
    )
    return logging

current_path = os.getcwd()
path = os.path.join(current_path,'back.log')
log = init_log(path)
log.info('这是第一个记录的日志信息')
log.warning('这是一个警告')
log.error('这是一个错误')
log.debug('这是一个debug')