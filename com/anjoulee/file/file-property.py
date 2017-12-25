# -*- coding: utf-8 -*-
#####Python 文件属性
### file.fileno()：文件描述符
### file.mode：文件打开权限
### file.encoding：文件编码格式
### file.closed：文件是否关闭
###
#####Python 标准文件
### sys.stdin：文件标准输入
### sys.stdout：文件标准输出
### sys.stderr：文件标准错误
###
###




import sys

print type(sys.stdin)

print sys.stdin
print sys.stdin.fileno()
###控制台输入
print raw_input(":")

print sys.stdout
print sys.stdout.write('10000')
print sys.stdout.fileno()

print sys.stderr
print sys.stderr.write('2000')
print sys.stderr.fileno()
print sys.stderr.mode
