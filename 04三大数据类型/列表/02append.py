# coding:utf-8
'''
append:将一个元素添加到当前的列表中
用法：list.append(new_item)
参数：
    new_item:添加进列表的新的元素（成员）
注意：
    被添加的元素只会被添加到末尾
    append函数是在原有列表的基础上，不需要额外添加新的变量

'''
books = []
print(id(books))

books.append('python入门课程')
print(books)
print(id(books))

number = 1.1
tuple_test = (1,)
dict_test = {'a':1}

books.append(number)
books.append(tuple_test)
books.append(dict_test)

print(books)
print(id(books))

# error: append() takes exactly one argument (3 given)
# books.append(number,tuple_test,dict_test)