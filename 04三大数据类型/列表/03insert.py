# coding:utf-8
'''
insert:将一个元素添加到当前列表的指定位置中
用法：
    list.insert(index, new_item)
参数：
    index:新的元素放在那个位置（数字）
    new_item:添加的新元素（成员）
注意：
    insert与append的区别
        append只能添加到列表的结尾，而insert可以选择任何一个位置
        如果insert传入的位置列表中不存在，则将新元素添加到列表结尾
        字符串、元素、列表 元素的位置是从0开始计算的

'''
students = [
    {'name': 'dewei', 'age': 22, 'sex': '男'},
    {'name': 'zengliwen', 'age': 23, 'sex': '女'},
    {'name': 'haha', 'age': 12, 'sex': '男'}
]
xiaoming = {
    'name': 'xiaoming',
    'age': 14,
    'sex': '男'
}
students.insert(0,xiaoming)
print(students)