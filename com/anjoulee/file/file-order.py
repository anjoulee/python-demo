# -*- coding: utf-8 -*-
#####Python 文件命令行参数
### sys模块提供sys.argv属性，通过属性可以得到命令行参数；
### sys.argv：字符串组成的列表


import sys



if __name__ == '__main__':
    print len(sys.argv)
    for arg in sys.argv:
        print arg
