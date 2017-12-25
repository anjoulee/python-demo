# -*- coding: utf-8 -*-

###正则表达式



###     '*'                  匹配前一个字符0次或者无限次
###     '+'                  匹配前一个字符1次或者无限次
###     '?'                  匹配前一个字符0次或者1次 [0-99]
###     '{m} / {m,n}'        匹配前一个字符m次或者n次
###     '*? / +? / ??'       匹配模式变为非贪婪（尽可能少匹配字符）


import re

ma = re.match(r'[A-Z][a-z]', 'Aa')
print ma.group()

ma = re.match(r'[A-Z][a-z]*', 'A')
print ma.group()

ma = re.match(r'[A-Z][a-z]*', 'Aaasdfads')
print ma.group()

ma = re.match(r'[A-Z][a-z]*', 'Aa1')
print ma.group()

ma = re.match(r'[_a-zA-Z]+[_\w]*', '_hta11')
print ma.group()

ma = re.match(r'[1-9]?[0-9]*', '99')
print ma.group()
ma = re.match(r'[1-9]?[0-9]*', '0-9')
print ma.group()

ma = re.match(r'[\w]{6}', 'abc123')
print ma.group()
# ma = re.match(r'[\w]{6}', 'abc12')
# print ma.group()
# ma = re.match(r'[\w]{6}', 'abc124')
# print ma.group()
ma = re.match(r'[\w]{6}@163.com', 'abc123@163.com')
print ma.group()
ma = re.match(r'[\w]{6,10}@163.com', 'abc1234567@163.com')
print ma.group()


ma = re.match(r'[0-9][a-z]*', '1bc')
print ma.group()
ma = re.match(r'[0-9][a-z]*?', '1bc')
print ma.group()
ma = re.match(r'[0-9][a-z]+?', '1bc')
print ma.group()
ma = re.match(r'[0-9][a-z]??', '1bc')
print ma.group()