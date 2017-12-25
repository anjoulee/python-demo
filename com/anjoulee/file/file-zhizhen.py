# -*- coding: utf-8 -*-
#####文件指针

### seek(offset[,whence])：移动文件指针
###      offset：偏移量，可以为负数
###      whence：偏移相对位置


###  Python 文件指针定位方式：
###   os.SEEK_SET：相对文件起始位置  0
###   os.SEEK_CUR：相对文件当前位置  1
###   os.SEEK_END：相对文件结尾位置  2

import os

f = open('imooc.txt', 'r+')
print f.tell()

print f.read(3)
print f.tell()

##重新定位指针--开头
f.seek(0, os.SEEK_SET)
print f.tell()


##重新定位指针--结尾
f.seek(0, os.SEEK_END)
print f.tell()


##重新定位指针--当前
f.seek(-5, os.SEEK_CUR)
print f.tell()

f.close()
