# coding: utf-8
# Python2.7
from math import sqrt

i = 2 + 2  # do something difficult
print type(i), i
i = sqrt(i)
print type(i), i
i = str(i)
print type(i), i
i = [i, i]
print type(i), i
print type(i[0])
print type(i[0][0])
