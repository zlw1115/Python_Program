# coding:utf-8
'''
字符串、列表和元素
从最左边记录的位置就是索引
索引用数字表示，起始从0开始
所引用来对单个元素进行访问，切片则对一定范围内的元素进行访问
切片通过冒号在中括号内把相隔的两个索引查找出来
左含，右不含
'''
numbers = [1,2,3,4,5,6,7,8,9]
print(numbers)
print(len(numbers)-1)
print(numbers[8])
print(id(numbers))
print('获取列表完整数据：',numbers[:])
print('另一种获取完整列表的方法：',numbers[0:])
print('第三种获取列表的方法',numbers[0:-1])
print('列表的反序：',numbers[::-1])
print('列表的反向获取：',numbers[-3:])
print('步长获取切片：',numbers[::2])
print('通过切片生成空列表',numbers[0:0])
'''
列表的索引，获取与修改
list[index] = new_item
数据的修改只能存在索引范围内
'''
numbers[3] = 'code'
print(numbers)
# numbers[9] = 10
# print(numbers)
numbers[2:5] = 'a', 'b', 'c'
print(numbers)
numbers[2:5] = ['a', 'b', 'c']
print(numbers)

print(numbers.index('c'))
'''
pop：通过索引删除并获取列表的元素
用法：
    list.pop(index)
参数：
    index：删除列表的第几个索引
        函数会删除该索引的元素并返回
        如果传入的index索引不存在则报错
        
del 通过del删除索引
del list[index]
    直接删除 无返回值
    如果index（索引）不存在则报错
'''
item = numbers.pop(4)
print(item,numbers,len(numbers))

del numbers[4]
print(numbers)
'''
索引切片在元组中的特殊性
    可以和列表一样获取索引与切片索引
    元组函数index和列表用法完全一致
    元素无法通过索引修改与删除元素
'''
tuple_test= (1,2,3)
# del tuple_test[2] # TypeError: 'tuple' object doesn't support item deletion
del tuple_test
print(tuple_test)