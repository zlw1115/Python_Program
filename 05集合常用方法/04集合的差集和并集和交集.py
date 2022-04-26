# coding:utf-8
'''
difference：返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合（方法的参数）中
用法：
    a_set.difference(b_set)
参数：
    b_set：当前集合需要对比的集合
返回值：
    返回原始集合与对比集合的差集（即a_set与b_set的差集）
'''
'''
intersection：返回两个或多个集合中都包含的元素，即交集
用法：
    a_set.intersection(b_set...)
参数：
    b_set...:与当前集合对比的1个或多个集合
返回值：
    返回元素集合与对比集合的交集
'''
'''
union:返回多个集合的并集，即包含了所有集合的元素，重复的集合只会出现一次
用法：
    a_set.union(b_set...)
参数：
    b_set...:与当前集合对比的1或多个集合
返回值：
    返回原始集合与对比集合的并集
    
'''
bin_rpm_name_list = ['libsecurity-conf','libsecurity1','libsecurity1-devel','libsecurity-conf-devel']
latest_bin_rpm_name_list =['libsecurity1','libsecurity1-devel','libsecurity1-debuginfo','libsecurity1-debugsource']
all_rpms = list(set(bin_rpm_name_list).union(set(latest_bin_rpm_name_list)))
print(all_rpms)
all_rpms = list(set(bin_rpm_name_list).intersection(set(latest_bin_rpm_name_list)))
print(all_rpms)