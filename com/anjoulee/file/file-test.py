# -*- coding: utf-8 -*-


###         mode           说明                    注意
###         'r'         只读方式打开              文件必须存在
###         'w'         只写方式打开              文件不存在创建文件
###         'a'         追加方式打开              文件存在则清空文件内容
###     'r+' / 'w+'     读写方式打开              文件不存在创建文件
###         'a+'        追加+读写方式打开
###    'rb','wb','ab','rb+','wb+','ab+':二进制方式打开

###文件不存在创建文件
f = open('1.txt', 'w')
f.close()

###追加方式打开
f = open('hello.py', 'a')
f.write('\nprint \'lilei2\'')
f.close()