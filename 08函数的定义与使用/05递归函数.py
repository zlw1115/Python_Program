# coding:utf-8
'''
递归函数

'''
count = 0
def test():
    global count
    count+=1
    if count != 5:
        print('count条件不满足，我要重新执行我自己，当前count是%d' % count)
        return test()
    else:
        print('count is %s' % count)
test()