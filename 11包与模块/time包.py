'''
时间戳
1970年1月1日00时00分至今的总毫秒（秒）数
timestamp
float

time模块
时间处理，转换时间格式
生成时间戳函数 time
获取本地时间函数，localtime
暂停函数sleep
time中的strftime与strptime

生成时间戳函数
导入包：
    import time
使用方法：
    time.time()
返回值：
    秒级别的浮点类型
举例：
    12837736.1231212

获取本地时间的localtime
导入包：
    import time
使用方法：
    time.localtime(timestamp)
参数介绍：
    timestamp：时间戳（可不传）

暂停函数sleep
导入包：
    import time
使用方法：
    time.sleep(s)
参数介绍：
    s：暂停秒数

time中的strftime
导入包：
    import time
使用方法：
    time.strftime(format,t)
    time.strptime(time_str,format)
参数介绍：
    format：格式化规范
    t:time.localtime对应的时间类型

    time_str:符合时间格式的字符串
    format：确保与time_str 一致的格式化标准
'''
import time

now = time.time()
print(now,type(now))
time_obj = time.localtime(now)
print(time_obj,type(time_obj))
time.sleep(5)
current_time_obj = time.localtime()
print(current_time_obj)

print(time.time() * 1000) #毫秒
print(time.time())

# for i in range(10):
#     print(i)
#     time.sleep(1)

'''
datetime中生成时间戳函数
导入包：
    import datetime
使用方法：
    now = datetime.datetime.now()
    now_timestamp = datetime.datetime.timestamp(now)
参数介绍：
    now:datetime时间对象
返回值：
    now转成的now_timestamp时间戳
    
datetime时间戳转时间对象
导入包：
    import datetime
使用方法：
    datetime.datetime.fromtimestamp(timestamp)
参数介绍：
    timestamp时间戳
返回值：
    事件对象
'''