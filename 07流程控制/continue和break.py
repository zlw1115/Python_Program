'''
continue的功能：
    循环语法continue将停止本次数据循环，进入下一次循环
用法
while bool:
    continue

for item in iterable:
    continue
    print(item)
参数：
    continue属于语法，不需要加()即可执行
无参数
返回值：
    continue是语法，没有返回值

count = 1
while count < 5:
    print(count)
    continue
    count += 1

>>1,1,1....
'''

'''
break的功能：是循环正常停止循环（遍历），这时如果循环配合了else语句，else语句将不执行
用法：
while bool:
    break

for item in iterable:
    break
    print(item)
参数：
    break，不需要加()即可执行
无参数
返回值：
    break是语法，没有返回值

count = 1
while count < 5:
    print(count)
    count += 1
    break

>>1
'''
'''
continue与break通常伴随循环语句中的条件语句，满足某些条件可以继续执行，不满足某些条件提前结束循环
在while循环中，break语句优先于while逻辑体的判断
'''