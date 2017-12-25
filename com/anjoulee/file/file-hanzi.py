# -*- coding: utf-8 -*-


import codecs

f = codecs.open('hanzi.txt', 'w', 'utf-8')
print  f.encoding

f.write(u'李磊')
f.close()
