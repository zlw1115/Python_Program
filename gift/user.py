# coding:utf-8

'''
1.用户与管理员的有效验证
2.防止并发操作userjson与giftjson
3.用__gift_update替代抽奖函数中手动更改奖品数量
4.登陆体系优化
5.每日抽奖次数限制

'''
import os
import random

from base import Base
from common.error import (NotUserError,RoleError,UserActiveError,CountError)
from common.utils import timestamp_to_string

class User(Base):
    def __init__(self,username,user_json,gift_json):
        self.username = username
        self.gift_random = list(range(1,101))

        super().__init__(user_json,gift_json)
        self.get_user()

    # 当前用户
    def get_user(self):
        users = self._Base__read_users()

        if self.username not in users:
            raise NotUserError('not user %s' % self.username)

        current_user = users.get(self.username)

        if current_user.get('active') == False:
            raise UserActiveError('the user %s had not use' % self.username)

        if current_user.get('role') != 'normal':
            raise RoleError('permission by normal')

        self.user = current_user
        self.name = current_user.get('username')
        self.role = current_user.get('role')
        self.gifts = current_user.get('gifts')
        self.create_time = timestamp_to_string(current_user.get('create_time'))

    def get_gifts(self):
        gifts = self._Base__read_gifts()
        gifts_list = []
        for level_one,level_one_pool in gifts.items():
            for level_two,level_two_pool in level_one_pool.items():
                for gift_name,gift_info in level_two_pool.items():
                    gifts_list.append(gift_info.get('name'))
        # leve_one,level_two条件下，的gifts列表
        return gifts_list

    def choice_gift(self):
        self.get_user()
        # level1 get
        first_level,second_level = None,None
        level_one_count = random.choice(self.gift_random)
        if 1 <= level_one_count <= 50:
            first_level = 'level1'
        elif 51<=level_one_count<=80:
            first_level = 'level2'
        elif 81 <=level_one_count < 95:
            first_level = 'level3'
        elif level_one_count >= 95:
            first_level = 'level4'
        else:
            raise CountError('level_one_count need 0-100')

        gifts = self._Base__read_gifts()
        level_one = gifts.get(first_level) # 一级奖品池

        level_two_count = random.choice(self.gift_random)
        if 1 <= level_two_count <= 80:
            second_level = 'level1'
        elif 81<=level_two_count<95:
            second_level = 'level2'
        elif 95 <=level_two_count < 100:
            second_level = 'level3'
        else:
            raise CountError('level_two_count need 0-100')

        level_two = level_one.get(second_level) # 二级奖品池
        if len(level_two)==0:
            print('很可惜，您没有中奖')
            return
        gift_names = []
        print(level_two)
        for k,_ in level_two.items():
            gift_names.append(k)

        gift_name = random.choice(gift_names)
        gift_info = level_two.get(gift_name)
        if gift_info.get('count') == 0:
            print('很可惜，您没有中奖')
            return
        # 重新写入奖品
        gift_info['count'] -= 1
        level_two[gift_name] = gift_info
        level_one[second_level] = level_two
        gifts[first_level] = level_one
        self._Base__save(gifts,self.gift_json)
        # 重新写入用户
        self.user['gifts'].append(gift_name)
        self.update()
        print('恭喜您中奖了 %s' % gift_name)

    def update(self):
        users = self._Base__read_users()
        users[self.username] = self.user

        self._Base__save(users,self.user_json)

if __name__ == '__main__':
    gift_path = os.path.join(os.getcwd(),'storage','gift.json')
    user_path = os.path.join(os.getcwd(),'storage','user.json')
    user = User(username='xiaomu',user_json=user_path,gift_json=gift_path)
    user.choice_gift()