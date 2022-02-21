'''
exists path 文件或路径是否存在 os.path.exits('') bool类型
isdir  path 是否是路径 os.path.isdir('') bool类型
isabs path 是否是绝对路径 os.path.isabs('') bool类型
isfile path 是否是文件 os.path.isfile('') bool类型
join path,path* 路径字符串合并 os.path.join('') 字符串
split path 以最后一层路径为基准切割 os.path.split() 列表

'''
import os.path
print(dir(os.path))