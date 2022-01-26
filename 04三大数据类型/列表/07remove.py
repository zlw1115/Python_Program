# coding:utf-8

'''
remove:删除列表中的某个元素
用法：
    list.remove(item)
参数：
    item:准备删除的列表元素
注意：
    如果删除的成员（元素）不存在，会直接报错
    如果被删除的元素有多个，只会删除从左至右的第一个
    remove函数不会返回一个新的列表，而是在原先的列表中对元素进行删除

del 把变量删除
'''
shops = ['可乐','洗发水','可乐','牛奶','牛奶','牙膏','牙膏']
print('超市有这些物品：%s' % shops)
shops.remove('洗发水')
print('现在洗发水还剩%d件' % shops.count('洗发水'))

del shops
print(shops)