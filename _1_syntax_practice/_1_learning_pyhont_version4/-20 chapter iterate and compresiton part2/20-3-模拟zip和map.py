#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     20-3-模拟zip和map
   Description :
   Author :      'Sam Yong'
   date：          2018/7/11
-------------------------------------------------
   Change Activity:
                   2018/7/11:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

# def mymap(func, *seqs):
#     return [func(*args) for args in zip(*seqs)]
#
# print(mymap(abs, [-2, -1, -4, -5]))

# 编写自己的zip
# print('*' * 20)
# def myzip(*seqs, pad = None):
#     seqs = [list(S) for S in seqs]
#
#     print(seqs)
#     #val = [(x, y) for x in seqs[0] for y in seqs[1]] # 这个是每个都有的，并不是一个对一个
#     var = []
#     print(val)
# S1, S2 = 'abc', '1234'
# print('*' * 20)
# print(myzip(S1, S2))
# seqs = [['a', 'b', 'c'], ['1', '2', '3', '4']]
# touple 是两个list

seqs = [['a', 'b', 'c'], ['1', '2', '3', '4']]
var = all(seqs) # all 检测是否含有 0 或者None
while all(seqs):
    app = []
    for S in seqs:
        app.append(S.pop(0)) # 遍历每个元素，将第一个pop出来，放到[]里面， 这就是一个链表了
    print(app)

print('end')

print('*' * 20)
def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    value = []
    while all(seqs):
        value.append(tuple([S.pop(0) for S in seqs])) # 这个就是列表解析，然后用tuple构建方式，然后获得内容

    return value

S1, S2 = 'abc', '1234'
value = myzip(S1, S2)
print(value)


print('*' * 20)
print('生成器方式')
def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    while all(seqs):
        yield (tuple([S.pop(0) for S in seqs])) # 这个就是列表解析，然后用tuple构建方式，然后获得内容

S1, S2 = 'abc', '1234'
value = myzip(S1, S2)
print(list(value))


print('*' * 20)
print('最大最小值')
def myzip(*seqs):
    minlen = min(len(S) for S in seqs)
    return [tuple(S[i] for S in seqs) for i in range(minlen)]

S1, S2 = 'abc', '1234'
value = myzip(S1, S2)
print(value)

print('*' * 20)
print('最大最小值,生成器方式')
def myzip(*seqs):
    minlen = min(len(S) for S in seqs)
    return (tuple(S[i] for S in seqs) for i in range(minlen))

S1, S2 = 'abc', '1234'
value = myzip(S1, S2)
print(list(value))