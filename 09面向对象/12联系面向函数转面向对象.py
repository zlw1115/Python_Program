# coding:utf-8

'''
学生信息库

def check_user_info(**kwargs):检查数据结构
def get_all_students()：获取全部学生信息
def add_student(**kwargs)：增加一个学生信息
def delete_student(student_id):删除一个学生
def update_student(student_id, **kwargs):更新一个学生信息
def get_user_by_id(student_id)：根据id获取学生信息
def search_users(**kwargs):根据某一键值对查找学生
'''
class StudentInfo(object):
    def __init__(self,studets):
        self.students = studets

    def get_by_id(self,student_id):
        if student_id not in self.students:
            print('学号为{}的同学不存在'.format(student_id))
            return
        student_info = self.students[student_id]
        return student_info

    def get_all(self):
        for id_, value in self.students.items():
            print('学号：{}，姓名：{},年纪：{}，性别:{}，班级：{}'.format(
                id_, value['name'], value['age'], value['sex'], value['class_number'])
            )
        return self.students

    def add(self,**student):
        check = self.check_user_info(**student)
        if check != True:
            print(check)
            return
        self.__add(student)

    def adds(self,new_students):
        for student in new_students:
            check = self.check_user_info(**student)
            if check !=True:
                print(check,student.get('name'))
                continue
            self.__add(**student)

    def __add(self, **student):
        new_id = max(self.students)+1
        self.students[new_id] = student

    def delete(self, student_id):
        if student_id not in self.students:
            print('{}并不存在'.format(student_id))
        else:
            student = students.pop(student_id)
            print('学号为：{}的{}同学已经被删除'.format(student_id, student['name']))

    def update(self,student_id, **kwargs):
        if student_id not in self.students:
            print('学号：{}不存在'.format(student_id))
        check = self.check_user_info(**kwargs)
        if check != True:
            print(check)
            return
        self.students[student_id] = kwargs

    def search(self,**kwargs):
        values = list(self.students.values())
        key = None
        value = None
        result = []
        if 'name' in kwargs:
            key = 'name'
            value = kwargs[key]
        elif 'age' in kwargs:
            key = 'age'
            value = kwargs[key]
        elif 'sex' in kwargs:
            key = 'sex'
            value = kwargs[key]
        elif 'class_number' in kwargs:
            key = 'class_number'
            value = kwargs[key]
        else:
            print('没有发现要搜索的关键字')
            return

        for user in values:
            if user[key] == value:
                result.append(user)
        return result

    def check_user_info(self,**kwargs):
        if 'name' not in kwargs:
            return '没有发现学生姓名'
        if 'age' not in kwargs:
            return '没有发现学生年龄'
        if 'class_number' not in kwargs:
            return '没有发现学生班号'
        if 'sex' not in kwargs:
            return '没有发现学生性别'
        return True



students = {
    1: {
        'name': 'dewei',
        'age': 33,
        'class_number': 'A',
        'sex': 'boy'
    },
    2: {
        'name': '小慕',
        'age': 10,
        'class_number': 'B',
        'sex': 'boy'
    },
    3: {
        'name': '小曼',
        'age': 18,
        'class_number': 'A',
        'sex': 'girl'
    },
    4: {
        'name': '小高',
        'age': 18,
        'class_number': 'C',
        'sex': 'boy'
    },
    5: {
        'name': '小云',
        'age': 18,
        'class_number': 'B',
        'sex': 'girl'
    }
}

if __name__ == '__main__':
    student_info = StudentInfo(students)
    user = student_info.get_by_id(1)
    print(user)
    student_info.add(name='zlw',age=23,class_number=2,sex='girl')
    print(student_info.get_all())
