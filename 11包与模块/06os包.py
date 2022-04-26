'''
import os

函数名         参数      介绍              举例                      返回值
getcwd        无        返回当前的路径      os.getcwd()             字符串
listdir       path      返回指定路径下所有
                        的文件和文件夹     os.listdir('c://Windows') 返回一个列表
makedir       pthon
              mode      创建多级文件夹     os.makedirs('d://imooc/py') 无
'''

'''
import os.path
exists path 文件或路径是否存在 os.path.exits('') bool类型
isdir  path 是否是路径 os.path.isdir('') bool类型
isabs path 是否是绝对路径 os.path.isabs('') bool类型
isfile path 是否是文件 os.path.isfile('') bool类型
join path,path* 路径字符串合并 os.path.join('') 字符串
split path 以最后一层路径为基准切割 os.path.split() 列表

传入的参数需为绝对路径
isdir  path 
isabs path 
'''
import os
import os.path

current_path = os.getcwd()
print(current_path)
print(os.path.isabs(current_path))
print(os.path.isabs('animal'))



new_path = '%s/test1' % current_path
if not os.path.exists(new_path):
    os.makedirs(new_path)

data = os.listdir(current_path)
print(data)

new_path2 = os.path.join(current_path, 'test2', 'abc')
print(new_path2)
if not os.path.exists(new_path2):
    os.makedirs(new_path2)
if not os.path.exists('test3'):
    os.makedirs('test3')

if os.path.exists('test2/abc'):
    os.removedirs('test2/abc')
# if os.path.exists('test3'):
#     os.rename('test3', 'test3_new')
# if os.path.exists('pip_image.py'):
#     os.rename('pip_image.py', 'pip3_image.py')
# if os.path.exists('%s/test3_new' % current_path):
#     os.rmdir('%s/test3_new' % current_path)
# if os.path.exists('test1'):
#     os.rmdir('test1')
#
print('----')
current_path = current_path + '/test.py'
print(os.path.isfile(current_path))
print(os.path.split(current_path))
print(os.path.isdir(os.path.split(current_path)[0]))
#
# print(dir(os.path))