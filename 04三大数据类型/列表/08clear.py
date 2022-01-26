# coding:utf-8
'''
clear:将当前列表中的数据情况
用法：list.clear()->该函数无参数，无返回值
'''
mixs = ['python',1,(1,),{'name':'zlw'}]
print(mixs,len(mixs))
mixs.clear() #比mix=[]性能更高
print(mixs,len(mixs))