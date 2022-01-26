# coding:utf-8
'''
copy:将当前的列表复制一份相同的列表，新列表与旧列表内容相同，但内存空间不同
用法：
    list.copy() => 该函数无参数，返回一个一模一样的列表
copy与二次赋值的区别
    二次赋值的变量与原始变量享有相同内存空间
    copy函数创建的新列表与原始列表不是一个内存空间不同享数据变更
    copy属于浅拷贝

浅拷贝
    通俗的说，我们有一个列表a，列表里的元素还是列表，当我们拷贝出新列表b后，无论是a
    还是b的内部的列表中的数据发生变化后，相互之间都会受到影响
深拷贝
    不仅对第一层数据进行了copy，对深层的数据也进行copy，原始变量和新变量完完全全不共享数据

'''
old_list = ['python', 'c', 'javascript']

new_list = old_list
new_list.append('java')
print(new_list)
print(old_list)
print(id(new_list))
print(id(old_list))

old_list.remove('c')
print(new_list,old_list)

del new_list
print(old_list) #依然存在

old_list_copy = ['python', 'c', 'javascript']
new_list_copy = old_list_copy.copy()
print(old_list_copy,new_list_copy)
new_list_copy.append('hh')
print(old_list_copy,new_list_copy)
print(id(old_list_copy),id(new_list_copy))