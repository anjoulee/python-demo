# coding:utf-8
###闭包测试
###返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()

print f1(), f2(), f3()


####返回闭包不能引用循环变量，改写count()函数，让它正确返回能计算1x1、2x2、3x3的函数。
def count2():
    fs = []
    for i in range(1, 4):
        def f(x):
            def g():
                return x * x

            return g

        r = f(i)
        fs.append(r)
    return fs


f1, f2, f3 = count2()

print f1(), f2(), f3()
