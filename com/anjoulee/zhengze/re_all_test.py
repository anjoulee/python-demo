# -*- coding: utf-8 -*-
######正则表达式测试,抓取网站图片

import re
import urllib2

req = urllib2.urlopen('http://www.imooc.com/course/list')

buf = req.read()
# print buf

listurl = re.findall(r'src=.+\.jpg', buf)
# print listurl

i = 0
for url in listurl:
    # url = url.replace('src=\"', 'http:')
    url = re.sub(r'src="', 'http:', url)
    print url

    f = open(str(i) + '.jpg', 'w')
    req = urllib2.urlopen(url)
    buf = req.read()
    f.write(buf)
    i += 1
