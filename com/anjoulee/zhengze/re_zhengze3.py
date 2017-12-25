# -*- coding: utf-8 -*-

###正则表达式


###******************边界匹配******************
###     '^'                  匹配字符串开头
###     '$'                  匹配字符串结尾
###     '\A / \Z'            指定的字符串匹配必须出现开头或则结尾

###******************分组匹配******************
###     ' | '                匹配左右任意一个表达式
###     '（ab）'              括号中表达式作为一个分组
###     '\<number>'          引用编号为num的分组匹配到的字符串
###     '(?P<name>)'         分组起一个别名
###     '?P=name'            引用别名为name的分组匹配字符串




import re

###******************边界匹配******************
ma = re.match(r'[\w]{4,10}@163.com', 'abc123@163.com')
print ma.group()

ma = re.match(r'[\w]{4,10}@163.com', 'abc123@163.comabc')
print '---' + ma.group()

ma = re.match(r'^[\w]{4,10}@163.com$', 'abc123@163.com')
print ma.group()

ma = re.match(r'\Aimooc[\w]*', 'imoocpython')
print ma.group()
# ma = re.match(r'\Aimooc[\w]*', 'iimoocpython')
# print ma.group()


###******************分组匹配******************
ma = re.match(r'abc|d', 'abc')
print ma.group()
ma = re.match(r'abc|d', 'd')
print ma.group()

ma = re.match(r'[1-9]?\d$', '9')
print ma.group()
ma = re.match(r'[1-9]?\d$', '99')
print ma.group()
# ma = re.match(r'[1-9]?\d$', '09')
# print ma.group()
ma = re.match(r'[1-9]?\d$|100', '100')
print ma.group()

ma = re.match(r'[\w]{4,6}@163.com', 'imooc@163.com')
print ma.group()
ma = re.match(r'[\w]{4,6}@(163|126).com', 'imooc@126.com')
print ma.group()


ma = re.match(r'<[\w]+>', '<book>')
print ma.group()
ma = re.match(r'<([\w]+>)', '<book>')
print ma.group()
ma = re.match(r'<([\w]+>)\1', '<book>book>')
print ma.group()
ma = re.match(r'<([\w]+>)\1', '<book>book>')
print ma.groups()
ma = re.match(r'<([\w]+>)[\w]+</\1', '<book>python</book>')
print ma.group()
ma = re.match(r'<([\w]+>)[\w]+</\1', '<book>python</book>')
print ma.groups()

ma = re.match(r'<(?P<mark>[\w]+>)[\w]+</(?P=mark)', '<book>python</book>')
print ma.group()