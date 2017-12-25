# -*- coding: utf-8 -*-

import re

###字符串查找
str1 = 'imooc videonum = 1000'
print str1.find('1000')

###正则表达式查找
info = re.search(r'\d+', str1)
print info
print info.group()

str1 = 'imooc videonum = 10000'
info = re.search(r'\d+', str1)
print info
print info.group()

str2 = 'c++=100,java=90,python=80'
info = re.search(r'\d+', str2)
print info.group()
info = re.findall(r'\d+', str2)
print info
print sum([int(x) for x in info])

#####替换
str3 = 'imooc videoum = 1000'
info = re.sub(r'\d+', '1001', str3)
print info

###替换函数
str4 = 'imooc videoum = 2000'


def add1(mach):
    val = mach.group()
    num = int(val) + 1
    return str(num)


print '===' + re.sub(r'\d+', add1, str4)

###分割
str5 = 'imooc:C C++ Java Python C# Go Hadoop'
print re.split(r':|', str5)
print re.split(r':| |', str5)
