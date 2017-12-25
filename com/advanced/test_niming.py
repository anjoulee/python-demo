# coding:utf-8
##匿名函数测试


###标准函数式
def is_not_empty(s):
    return s and len(s.strip()) > 0


print '函数式调用', filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])

###利用匿名函数简化
print '匿名函数调用', filter(lambda s: s and len(s.strip()) > 0, ['test', None, '', 'str', '  ', 'END'])
