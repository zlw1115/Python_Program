'''
modules 无 py启动时加载的模块 sys.modules() 列表
path 无 返回当前py环境路径 sys.path() 列表
exit arg 退出程序 sys.exit(0) 无
getdefaultencoding 无 获取系统编码 sys.getdefaultencoding() 字符串
platform 无 获取当前系统平台 sys.platform() 字符串
version(属性) 无 获取python版本 sys.version 字符串
argv *argv 程序外部获取参数 sys.argv 列表
'''
import sys
command = sys.argv[1]
if command == 'modules':
    modules = sys.modules
    print(modules)
elif command == 'path':
    path = sys.path
    print(path)
elif command == 'encoding':
    code = sys.getdefaultencoding()
    print(code)
elif command == 'platform':
    print(sys.platform)
elif command == 'version':
    print(sys.version)
else:
    print('not command')