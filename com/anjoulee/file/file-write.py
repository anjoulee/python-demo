# -*- coding: utf-8 -*-
#####文件写入


###文件写入方式
### write(str)：将字符串写入文件
### writelines(sequence of strings)：写多行文到文件，参数为可迭代对象
###
###
###


f = open('imooc.txt', 'w')
f.write('test write')
f.close()

f = open('imooc.txt', 'w')
f.writelines('112335522')
f.close()

f = open('imooc.txt', 'w')
f.writelines(('1', '2', '3'))
f.close()




###打开文件要及时关闭文件
list_f = []
for i in range(1025):
    list_f.append(open('imooc.txt', 'w'))
    print "%d:%d" % (i, list_f[i].fileno())