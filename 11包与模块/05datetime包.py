#coding:utf-8
'''
datetime
日期与时间的结合体-date and time
获取当前时间
获取时间间隔
将时间对象转成时间字符串
将字符串转成时间类型

'''
'''
获取当前时间
from datetime import datetime
import datetime
使用方法
datetime.now()
datetime.datetime.now()

获取时间间隔
导入包
from datetime import datetime
from datetime import timedelta # timedelta是函数（在datetime的__init__.py中定义或引入）
使用方法
timeobj = timedelta(days=0,seconds=0,microseconds=0,milliseconds=0,minutes=0,hours=0,week=0)

'''
from datetime import datetime
from datetime import timedelta

now = datetime.now()
print(now,type(now))

three_days = timedelta(days = 3)
after_three_day = now + three_days
print(after_three_day)

before_three_day = now - three_days
print(before_three_day)

one_hour = timedelta(hours=1)
before_one_hour = now - one_hour
print(before_one_hour)
'''
将时间对象转字符串
获取时间对象
from datetime import datetime
now = datetime.now()
时间转字符串：
date_str = now.strftime(format)
'''
now_str = now.strftime('%Y-%m-%d %H:%M:%S')
print(now_str,type(now_str))

'''
将时间字符串转成时间类型
获取时间模块
from datetime import datetime
时间字符串转时间类型：
datetime.strptime(tt,format)
参数介绍：
tt:符合时间格式的字符串
format：tt时间字符串匹配规则
'''
date_obj = datetime.strptime(now_str,'%Y-%m-%d %H:%M:%S')
print(date_obj,type(date_obj))
'''
时间格式符
%Y  完整的年份（如2022）
%m  月份（1-12）
%d  月中的某一天（1-31）
%H  一天中的第几个小时（24小时，0-23）
%I  一天中的第几个小时（12小时，01-12）
%M  当前的第几分（00-59）
%S  当前的第几秒（0-61）闰年多占2秒
%f  当前秒的第多少毫秒
%a  简化的星期，如星期三 Wed
%A  完整的星期，如星期三 Wednesday
%b  简化的月份，如二月 Feb
%B  完整的月份，如二月 February
%c  本地日期和时间，如Wed Feb 5 10:14:49 2020
%p  显示是上午还是下午，AM，PM
%j  一年中的第几天
%U  一年中的星期数
'''