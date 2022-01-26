# coding:utf-8
'''
add：用于集合中添加一个元素，如果集合中已经存在该元素则该函数不执行
用法：
    set.add(item)
参数：
    item:要添加到集合中的元素
返回值：
    无返回值
'''
a_list = ['python', 'c', 'c', 'c++']
a_set = set()
a_set.add(a_list[0])
a_set.add(a_list[1])
a_set.add(a_list[2])
a_set.add(a_list[3])

a_set.add(True)
a_set.add(None)

print(a_set)
'''
update:加入一个新的集合（或列表、元组、字符串），如新集合内的元素在原集合中存在则无视
用法：
    set.update(iterable)
参数：
    iterable：集合、列表、元组或字符串
返回值：
    无返回值，直接作用于原集合
'''
a_tuple = ('a','b','c')
a_set.update(a_tuple)
print(a_set)
a_set.update('python')
print(a_set) # ’p‘ 'y' 't' 'h' 'o' 'n'

'''
remove：将集合中的某个元素删除，如元素不存在将会报错
用法：
    set.remove(item) #注意是元素不是索引
参数：
    item：当前集合中的一个元素
返回值：
    无返回值，直接作用于原集合
    
clear:清空当前集合中的所有元素
用法：
    set.clear()
参数：
    无
返回值：
    无返回值，直接作用于原集合
    
del 删除集合


注意：
    集合无法通过索引获取元素
    集合无获取元素的任何方法
    集合只是用来处理列表或元组的一种临时类型，他不适合存储与传输
'''