# coding:utf-8
'''
sort:对当前列表按照一定规律进行排序
用法：
    list.sort(key=None, reverse=False)
参数：
    key-参数比较
    reverse - 排序规则，reverse = True降序，reverse = False升序（默认）
注意：
    列表中的元素类型必须相同，否则无法排序（报错）
'''
shu = '01老鼠'
niu = '02牛'
hu = '03虎'
tu = '04兔'
long = '05龙'
she = '06蛇'
ma = '07马'
ya = '08羊'
hou = '09猴'
ji = '10鸡'
gou = '11狗'
zhu = '12猪'
shengxiao = [gou,zhu,ma,ya,hu,tu,shu,niu,she,long,ji,hou]
print(shengxiao)
shengxiao.sort()
print(shengxiao)
shengxiao.sort(reverse=True)
print(shengxiao)
shengxiao.sort(reverse=True)#不再变化
print(shengxiao)
mix = [12,'zd',{'name':'zlw'}]
# mix.sort()
# print(mix)