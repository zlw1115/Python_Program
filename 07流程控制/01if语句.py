# ccoding:utf-8

info = 'my name is xiaoming'
info_list = info.split()
print(info_list)

if info_list[0] == 'xiaoming':
    info_list[0] = 'hh'
if info_list[1] == 'xiaoming':
    info_list[1] = 'hh'
if info_list[2] == 'xiaoming':
    info_list[2] = 'hh'
if info_list[3] == 'xiaoming':
    info_list[3] = 'hh'
print(info_list)