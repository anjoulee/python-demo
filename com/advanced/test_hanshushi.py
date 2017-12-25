# coding:utf-8
import math


###定义一个高阶函数
def add(x, y, f):
    return f(x) + f(y)


print '调用高阶函数:', add(-5, 9, abs)


###利用add(x,y,f)函数，计算x、y的平方根
def add(x, y, f):
    return f(x) + f(y)


print '利用add(x,y,f)函数，计算x、y的平方根:', add(25, 9, math.sqrt)


###假设用户输入的英文名字不规范，没有按照首字母大写，后续字母小写的规则，请利用map()函数，把一个list（包含若干不规范的英文名字）变成一个包含规范英文名字的list：
###输入：['adam', 'LISA', 'barT']
###输出：['Adam', 'Lisa', 'Bart']
def format_name(s):
    return s[0].upper() + s[1:].lower()


print "输入：['adam', 'LISA', 'barT']"
print '利用map()函数输出：', map(format_name, ['adam', 'LISA', 'barT'])


###Python内置了求和函数sum()，但没有求积的函数，请利用recude()来求积：
###输入：[2, 4, 5, 7, 12]
###输出：2*4*5*7*12的结果
def prod(x, y):
    return x * y


print "利用recude()来求积输入：[2, 4, 5, 7, 12]:\n", '输出：2 * 4 * 5 * 7 * 12的结果:', reduce(prod, [2, 4, 5, 7, 12])


###请利用filter()过滤出1~100中平方根是整数的数，即结果应该是：[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#### filter() 接收的函数必须判断出一个数的平方根是否是整数，而 math.sqrt()返回结果是浮点数。
def is_sqr(x):
    res = int(math.sqrt(x))
    return res * res == x


print 'filter() 接收的函数必须判断出一个数的平方根是否是整数:', filter(is_sqr, range(1, 101))


###对字符串排序时，有时候忽略大小写排序更符合习惯。请利用sorted()高阶函数，实现忽略大小写排序的算法。
###输入：['bob', 'about', 'Zoo', 'Credit']
###输出：['about', 'bob', 'Credit', 'Zoo']
###对于比较函数cmp_ignore_case(s1, s2)，要忽略大小写比较，就是先把两个字符串都变成大写（或者都变成小写），再比较。
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 > u2:
        return 1
    if u1 < u2:
        return -1
    return 0


print '利用sorted()高阶函数，实现忽略大小写排序的算法:', sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)


###请编写一个函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积
###先定义能计算乘积的函数，再将此函数返回
def calc_prod(lst):
    def prod():
        def f(x, y):
            return x * y

        return reduce(f, lst, 1)

    return prod


f = calc_prod([1, 2, 3, 4])
print '先定义能计算乘积的函数，再将此函数返回：', f()



