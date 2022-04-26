# coding:utf-8
import os
from base import Base
from common.error import NotUserError,UserActiveError,RoleError

class Admin(Base):
    def __init__(self,username,user_json,gift_json):
        self.username = username
        super().__init__(user_json,gift_json)
        self.get_user()

    def get_user(self):
        users = self._Base__read_users()
        current_user = users.get(self.username)
        if current_user == None:
            raise NotUserError('not user %s' % self.username)
        if not current_user.get('active'):
            raise UserActiveError('the user %s had not active' % self.username)

        if current_user.get('role') != 'admin':
            raise RoleError('you are not admin')

        # 管理员的gifts属性不重要
        self.user = current_user
        self.role = current_user.get('role')
        self.name = current_user.get('username')
        self.active = current_user.get('active')

    def __check(self,message):
        self.get_user()
        # 为啥又判断一次
        if self.role != 'admin':
            raise Exception(message)

    # 增加用户
    def add_user(self,username,role):
        self.__check('premission')

        self._Base__write_user(username=username,role=role)

    # 更改用户active属性
    def update_user_active(self,username):
        self.__check('premission')
        self._Base__change_active(username=username)

    # 更改用户role属性
    def update_user_role(self,username,role):
        self.__check('premission')
        self._Base__change_role(username=username,role=role)

    # 写gift
    def add_gift(self,first_level,second_level,
                   gift_name,gift_count):
        self.__check('premission')
        self._Base__write_gift(first_level=first_level,second_level=second_level,
                                gift_name=gift_name,gift_count=gift_count)

    # 删除gift
    def delete_gift(self,first_level,second_level,
                   gift_name):
        self.__check('premission')
        self._Base__delete_gift(first_level=first_level,second_level=second_level,gift_name=gift_name)

    # 更改gift的count属性
    def update_gift(self,first_level,second_level,
                   gift_name,gift_count):
        self.__check('premission')
        self._Base__gift_update(first_level=first_level,second_level=second_level,gift_name=gift_name,gift_count=gift_count,is_admin=True)


if __name__ == '__main__':
    gift_path = os.path.join(os.getcwd(),'storage','gift.json')
    user_path = os.path.join(os.getcwd(),'storage','user.json')
    admin = Admin('zlw',user_path,gift_path)
    # print(admin.name,admin.role)
    # admin.update_user_role(username='xiaomu',role='normal')
    admin.add_gift(first_level='level1',second_level='level1',
                   gift_name='pencli',gift_count=200)