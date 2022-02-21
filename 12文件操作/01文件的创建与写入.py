'''
内置函数open获取文件对象
功能：
    生成文件对象，进行创建，读写操作
用法：
    open(path,mode)
参数说明：
    path：文件路径
    mode：操作模式
返回值：
    文件对象

模式     介绍
w       创建文件
w+      创建或追加内容
wb      二进制形式创建文件
wb+     二进制形式创建或追加内容
a       追加内容
a+      读写模式的追加
ab+     二进制形式读写追加

文件对象的操作方法
方法名         参数             介绍      举例
write         Message        写入信息     f.write('hello\n')
writelines    Message_list    批量写入    f.writelines(['hello\n','world\n'])
close         无              关闭并保存文件 f.close()

操作完成后，必须使用close方法
'''
import os
def create_package(path):
    if os.path.exists(path):
        raise Exception('%s已经存在' % path)
    os.makedirs(path)
    init_path = os.path.join(path,'__init__.py')
    f = open(init_path,'w')
    f.write('# coding:utf-8\n')
    f.close()

class Open(object):
    def __init__(self,path,mode='w',is_return=True):
        self.path = path
        self.mode = mode
        self.is_return = is_return

    def write(self,message):
        try:
            f = open(self.path,mode = self.mode)
            if self.is_return:
                if not message.endswith('\n'):
                    message = '%s\n' % message
            f.write(message)
        except Exception as e:
            print(e)
        finally:
            f.close()

    def read(self,is_strip=True):
        result = []
        with open(self.path,mode = self.mode) as f:
            # data = f.read()
            data = f.readlines()
        for line in data:
            if is_strip == True:
                temp = line.strip()
                if temp != '':
                    result.append(temp)
            else:
                if line != '':
                    result.append(line)
        return result

if __name__ == '__main__':
    current_path = os.getcwd()
    # path = os.path.join(current_path,'test1')
    # create_package(path)
    open_path = os.path.join(current_path,'b.txt')
    o = Open(open_path, 'r')
    # o.write('你好')
    data = o.read(is_strip=False)
    print(data)
