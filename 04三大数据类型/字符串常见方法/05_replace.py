# coding:utf-8
'''
replace:将字符串中的old（旧元素）替换成new（新元素），并能指定替换的数量
用法：
    newstr = string.replace(old.new,max)
参数：
    old:被替换的元素
    new:替换old的新元素
    max:可选，代表替换几个，默认全部替换全部匹配的old元素
'''
info =( '赞同，不过手机端就够了，而且拥有较大的流量入口。网页端的话，估计在开发中，不过应该是指电脑的夸克搜索引擎吧，'
        '而不是浏览器？网页端浏览器的话，夸克如果有我会尝试一下，不过目前谷歌浏览器在PC端基本是无敌的存在，非常全面好用，'
        '如果有个梯子可以保存各种记录和书签方便。最近Micosoft的Edge也更新了，感觉用的多了起来'
        '作者：Future小哥哥'
        '链接：https://www.zhihu.com/question/351223179/answer/1238491270'
        '来源：知乎0'
        '著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处')
a = '不过'
b = '浏览器'
c = '*'
# test = info.replace(a, c)
# test = test.replace(b, c)
# print(test)

test = info.replace(a, c).replace(b, c)
print(test)