#! /usr/bin/env python
# -*- coding: utf-8 -*-


def readGPS(filename):
    with open(filename) as fi:
        text = fi.readlines()
    data = [[int(t), str(c), float(x), float(y)]
            for l in text for _, t, c, x, y in (l.split(),)]
    # data = []
    # for l in text:
    #     _, t, c, x, y = l.split()
    #     data.append([int(t), str(c), float(x), float(y)])
    return text, data

# 1


print u"Handbauer Péter"

# 2

text1, data1 = readGPS("cars1.txt")
print len(data1)

# 3

cars1 = {d[1] for d in data1}
print len(cars1)

# 4

print max([d[2] for d in data1])

# 5

# data1_ysorted = sorted(data1, cmp=lambda a, b: int(a[3] - b[3]))
# print data1_ysorted[-1][1]

print max(data1, key=lambda a: a[3])[1]

# 6

text2, data2 = readGPS("cars2.txt")
cars_list = [d[1] for d in data2]
cars2 = set(cars_list)
cars2_max = max(cars2, key=lambda c: cars_list.count(c))
print cars2_max

# 7

maxcar_tsorted = sorted(
    [d for d in data2 if d[1] == cars2_max], key=lambda l: l[0])
print "{2} {3}".format(*maxcar_tsorted[-1])

# 8

fake_rec = (d for d in data2 if sum(map(int, str(d[0]))) == 42).next()
print fake_rec[1]

# note: comleted in approx. 35-40 minutes
