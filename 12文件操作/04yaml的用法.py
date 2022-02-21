'''
yaml文件的介绍
xxx.yaml
name:           key
 xiamu          value
age:
 10
xinqing:
 - haha         列表
 - heihei
new:
 a:b            dict
 c:1
'''
'''
pyyaml模块
pip install pyyaml
import yaml
用法：
    f = open(yaml_file,'r')
    data = yaml.load(f.read()) #字典
    f.close()
'''
import yaml

def read(path):
    with open(path,'r') as f:
        data = f.read()
    result = yaml.load(data,Loader=yaml.FullLoader)
    return result

if __name__ == '__main__':
    result = read('muke.yaml')
    print(result)
    print(dir(yaml))