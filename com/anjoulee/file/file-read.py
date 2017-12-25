# -*- coding: utf-8 -*-
#####文件读取


###文件读取方式
### read([size])：读取文件（读取size个字节，默认读取全部）
### readline([size])：读取一行
### readlines([size])：读取完文件，返回每一行所组成的列表
###                    并没有去完，只读了接近io.DEFAULT_BUFFER_SIZE个缓冲字节（8192）
### iter：使用迭代器读取文件


f = open('1.txt')
# print f.readline()
# print f.readline(2)
print f.readlines()
f.close()

import io

print io.DEFAULT_BUFFER_SIZE

###迭代器读取
f = open('1.txt')
iter_f = iter(f)
lines = 0
for line in iter_f:
    lines += 1
print lines
f.close()



###打开文件要及时关闭文件
list_f = []
for i in range(1025):
    list_f.append(open('imooc.txt', 'w'))
    print "%d:%d" % (i, list_f[i].fileno())