# -*- coding: utf-8 -*-

###正则表达式


###     '.'             匹配任意字符（除了\n）
###     '[...]'         匹配字符集
###     '\d / \D'       匹配数字 / 非数字
###     '\s / \S'       匹配空白 / 非空白
###     '\w / \W'       匹配单词字符[a-zA-Z0-9] / 非单词字符


import re

ma = re.match(r'a', 'a')
print ma.group()
ma = re.match(r'a', 'b')
print type(ma)

ma = re.match(r'.', 'b')
print ma
print ma.group()

ma = re.match(r'.', '0')
print ma.group()

ma = re.match(r'{.}', '{a}')
print ma.group()

ma = re.match(r'{.}', '{0}')
print ma.group()

ma = re.match(r'{..}', '{01}')
print ma.group()

ma = re.match(r'{[abc]}', '{a}')
print ma.group()
ma = re.match(r'{[a-z]}', '{d}')
print ma.group()

ma = re.match(r'{[a-zA-Z]}', '{A}')
print ma.group()

ma = re.match(r'{[a-zA-Z0-9]}', '{9}')
print ma.group()

ma = re.match(r'{[\w]}', '{a}')
print ma.group()

# ma = re.match(r'{[\W]}', '{k}')
# print ma.group()

ma = re.match(r'\[[\w]\]', '[0]')
print ma.group()
