# coding:utf-8
'''
count:返回当前列表中某个元素的个数
用法：
    inttype = list.count(item)
参数：
    item:你想查询个数的元素
注意：
    如果查询的成员（元素）不存在，则返回0
    列表只会检查完整元素是否存在需要计算的内容
'''
animals = ['小猫','小狗','龙猫','鹦鹉','小猫']
cat = animals.count('小猫')
dog = animals.count('小狗')
l_cat = animals.count('龙猫')
print('我家的院子里有很多动物')
print('其中小猫有 %d 只' % cat)
print('小狗有 %d 只'% dog)
print('龙猫有 %d 只' % l_cat)

dict_animals = [
    {'name':'cat'},
    {'name':'dog'},
    {'name':'cat'}
]

dog_dict_count = dict_animals.count({'name':'cat'})
print(dog_dict_count)

animals_tuple = ('小猫','小狗','龙猫','鹦鹉','小猫')
cat = animals_tuple.count('小猫')
dog = animals_tuple.count('小狗')
l_cat = animals_tuple.count('龙猫')
print('我家的院子里有很多动物,其中小猫有 %d 只,小狗有 %d 只,龙猫有 %d 只' % (cat,dog,l_cat))
