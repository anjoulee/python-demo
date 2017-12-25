# coding = utf-8
import numpy as np

height = [1.73, 1.68, 1.71, 1.89, 1.79]
print height
np_height = np.array(height)
print np_height

weight = [65.4, 58.6, 69.5, 88.5, 66.8]
print weight

np_weight = np.array(weight)
print np_weight

print np_weight / np_height ** 2

fam = np.array([[1.73, 1.68, 1.71, 1.89, 1.79], [65.4, 58.6, 69.5, 88.5, 66.8]])
print fam[0][2]

func = lambda x: x ** 2
print func(20)
a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print map(func, a_list)
