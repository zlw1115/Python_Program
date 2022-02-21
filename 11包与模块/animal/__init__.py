# coding:utf-8

'''
在包中__init__中导入其他的模块或包，只需在包或模块前加.
'''
from .cat.action import run as cat_run
from .dog.action import run as dog_run
from .cat.action import Cat
from .test import test_method

