# -*- coding: utf-8 -*-

###使用OS模块打开文件
### os.open(filename,flag[,mode])：打开文件
### flag：打开文件方式
### os.O_CREATE：创建文件
### os.O_RDONLY：只读方式打开
### os.O_WRONLY：只写方式打开
### os.O_RDWR：读写方式打开

###使用OS模块对文件操作
### os.read(fd,buffersize)：读取文件
### os.write(fd,string)：写入文件
### os.lseek(fd,pos,how)：文件指针操作
### os.close(fd)：关闭文件



import os

##创建文件并赋予读写权限
fd = os.open('imooc1.txt', os.O_CREAT | os.O_RDWR)
##写入文件内容
n = os.write(fd, 'imooc')
##重定位指针
I = os.lseek(fd, 0, os.SEEK_SET)
print I
##重定位后读取文件
str = os.read(fd, 5)
print str
os.close(fd)


### OS模块方法介绍
### access(path,mode)           判断该文件权限：F_OK存在；权限：R_OK,W_OK, X_OK
### listdir(path)               返回当前目录下所有文件组成的列表
### remove(path)                删除文件
### rename(old,new)             修改文件或目录名
### mkdir(path[,mode])          创建目录
### makedirs(path[,mode])       创建多级目录
### removedirs(path)            删除多级目录
### rmdir(path)                 删除目录（目录必须为空目录）

print os.access('imooc.txt',os.R_OK)
print os.listdir('E:\\python\\python-demo\\com\\anjoulee\\file')
#print os.mkdir('file3')
#print os.makedirs('E:\\python\\python-demo\\com\\anjoulee\\file\\file2')



### os.path模块方法介绍
### exists(path)                当前路径是否存在
### isdir(s)                    是否是一个目录
### isfile(path)                是否是一个文件
### getsize(filename)           返回文件大小
### dirname(p)                  返回路径的目录
### basename(p)                 返回路径的文件名

print 'os.path模块方法介绍'

print os.path.exists('file3')
print os.path.isdir('imooc.txt')
print os.path.isfile('imooc.txt')
print os.path.getsize('imooc.txt')
print os.path.basename('imooc.txt')
print os.path.dirname('E:\\python\\python-demo\\com\\anjoulee\\file\\file2')
