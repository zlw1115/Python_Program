'''
功能：
    通过从某个包中找到对应的模块
用法：
    from package import module
参数：
    package：来源的包名
    module：包中的目标模块

'''
from animal import dog_run,cat_run
# from animal import cat_run
from animal.cat.action import cat_name
# 导入类
# from animal.cat.action import Cat
from animal import  Cat
cat = Cat('hh')
print(cat.cat_name)
print(cat_run())
print(dog_run())
print(cat_name)