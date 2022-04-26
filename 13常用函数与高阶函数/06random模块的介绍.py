# coding:utf-8
'''
random.random
    随机返回0-1之间的浮点数

random.uniform
    产生一个a，b区间的随机浮点数

random.randint
    产生一个a，b区间的随机整数

random.choice
    返回对象中的一个随机元素

random.sample
    随机返回对象中指定的元素

random.randrange
    获取区间内的一个随机数
'''
import random

gifts = ['iphone', 'ipad', 'car', 'tv']
def choice_gifts():
    gift = random.choice(gifts)
    print('你得到了%s' % gift)


def choice_gift_new():
    count = random.randrange(0,100,1)
    if 0 <= count <= 50:
        print('你中了一个iphone')
    elif 50 < count <= 70:
        print('你中了一个ipad')
    elif 70 < count <= 90:
        print('你中了一个tv')
    elif  count >= 91:
        print('你中了一个car')

if __name__ == '__main__':
    # choice_gifts()
    choice_gift_new()