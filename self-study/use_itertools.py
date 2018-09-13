#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

natuals = itertools.count(1)
for n in natuals:
    print(n)
    if n >= 100:
        break

cs = itertools.cycle('ABC')
t = 10
for c in cs:
    print(c)
    t = t - 1
    if t == 0:
        break
        
ns = itertools.repeat('D', 3)
for n in ns:
    print(n)

natuals = itertools.count(1)
nss = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(nss))

for c in itertools.chain('ABC', 'XYZ'):
    print(c)

for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))

# 小结

# itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。