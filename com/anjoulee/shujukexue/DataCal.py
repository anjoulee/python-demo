fam = ['a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5, 'f', 6, 'g', 7, 'h', 8, 'i', 9]
print fam
print fam[2:4]
fam[2:4] = ['bb', 22]
print fam
print fam[2:4]

print fam + ['00', 0]

del (fam[1])
print fam

print "###################################"
x = ['a', 'b', 'c']
print x
y = x
y[1] = 'z'
print y
print x

print "###################################"

z = list(x)
print z
z = x[:]
print  z

z[1] = 'h'
print x

print z
