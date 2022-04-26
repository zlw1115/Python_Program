#coding:utf-8
'''
findall(pattern,string [,flags])
查找字符串中所有（非重复）出现的正则表达式模式，并返回一个匹配列表

search(pattern, string, flags=0)
使用可选标记搜索字符串中第一次出现的正则表达式模式。
如果匹配成功，则返回匹配对象，如果失败，则返回None

group()与groups()
group(num)返回整个匹配对象，或者编号为num的特定子组

groups():返回一个包含所有匹配子组的元组（如果没有成功匹配，则返回一个空元组）

split()正则替换
split(pattern,string,max=0)
根据正则表达式的模式分隔符，split函数将字符串分割为列表，然后返回成功匹配的列表，
分隔最多操作max次（默认分割所有匹配成功的位置）

match(pattern,string,flags=0)
尝试使用带有可选的标记的正则表达式的模式来匹配字符串。如果匹配成功，就返回匹配第对象；
如果失败，就返回None

compile(pattern,flags=0)
定义一个匹配规则的对象
'''
'''
re的额外匹配要求
属性                      要求
re.I,re.IGNORECASE        不区分大小写的匹配
re.L,re.LOCALE            根据所使用的本地语言环境通过\w,\W,\s,\S实现匹配
                          (unicode-python2时代，可以理解为通用模式，类似utf-8)
re.M,re.MULTILINE          ^和$分别匹配目标字符串中行的起始和结尾，而不是严格匹配整个
                            字符串本身的起始和结尾
re.S,rer.DOTALL             "."（点号）通常匹配除了\n（换行符）之外的所有单个字符;该标记表示"."（点号）能够匹配全部字符
re.X,re.VERBOSE             忽略规则表达式中的空白和注释
'''
import re

def check_url(url):
    re_g = re.compile('[a-zA-Z]{4,5}://\w*\.*\w+\.\w+')
    print('test',re_g)
    result = re_g.findall(url)
    if len(result) != 0:
        return True
    else:
        return False

def get_url(url):
    re_g = re.compile('[https://|http://](\w*\.*\w+\.\w+)')
    result = re_g.findall(url)
    if len(result) != 0:
        return result[0]
    else:
        return ''


def get_email(data):
    re_g = re.compile('.+@.+\.[a-zA-Z]+')
    result = re_g.findall(data)
    return result


html = ('<div class="s-top-nav" style="display:none;">'
        '</div><div class="s-center-box"></div>')


def get_html_data(data):
    re_g = re.compile('style="(.*?)"')
    result = re_g.findall(data)
    return result

def get_all_data_html(data):
    re_g = re.compile('="(.+?)"')
    result = re_g.findall(data)
    return result


if __name__ == '__main__':
    result = check_url('http://www.baidu.com/')
    print(result)
    result = get_url('https://www.baidu.com/')
    print(result, 'get_url')
    result = get_email('dewei@imooc.net')
    print(result)
    print('==')
    result = get_html_data(html)
    print(result)
    result = get_all_data_html(html)
    print('+++')
    print(result)
    re_g = re.compile(('<div class="(.*?)" style="(.*?)">'
        '</div><div class="(.*?)"></div>'))
    result = re_g.search(html)
    print(result)
    print(result.groups())
    print(result.group(1))
    print(result.group(2))
    print(result.group(3))
    # print(result.group(4))
    re_g = re.compile('\s')
    result = re_g.split(html)
    print('++++')
    print(result)

    re_g = re.compile('<div class="(.*?)"')
    result = re_g.match(html)
    print(result.span())
    print(html[: 22])
