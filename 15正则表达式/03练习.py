# conding:utf-8
import re

url = 'https://www.imooc.com/'

def check_url(url):
    result = re.findall('[a-zA-Z]{4,5}://\w*\.*\w+\.\w+',url)
    if len(result) !=0:
        return True
    else:
        return False
def get_url(url):
    result = re.findall('https://(\w*\.*\w+\.\w+)',url)
    if len(result) !=0:
        return result[0]
    else:
        return ''

def get_email(data):
    # result = re.findall('[0-9a-zA-Z_]+@[0-9a-zA-Z]+\.[a-zA-Z]+',data)
    result = re.findall('.+@.+\.[a-zA-Z]+',data)
    return result

if __name__ == '__main__':
    result = check_url('https://www.imooc.com/')
    result = get_url('https://www.imooc.com/')
    result = get_email('zlw@zlw.com')
    print(result)