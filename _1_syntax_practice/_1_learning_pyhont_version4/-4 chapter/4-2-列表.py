#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     4-2-列表
   Description :
   Author :      'Sam Yong'
   date：          2018/6/29
-------------------------------------------------
   Change Activity:
                   2018/6/29:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

L = ['aa', 'cc', 'dd', 'bb']
print(L)

L.sort()  # 升序排序
print(L)

L.reverse()  # 翻转
print(L)

#print(L[4])  # list 有边界检查

# 嵌套
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(M)

# 列表解析（list comprehension expression)
## 如果要取出M 的第二列
# 第一种方式
L = []
for row in M:
     L.append(row[1])

print(L)

# 第二种方式 ， 列表推倒式子
print([row[1] for row in M])

# 找出矩阵中第三列的奇数
print([row[2] for row in M if row[2] % 2 == 1])

# 数据分析工具NumPy系统


#  生成器语法？
G = (sum(row) for row in M)
print(G)

# 生成器创建list
L = list(map(sum, M))
print(L)

# 生成器创建集合
Set = {sum(row) for row in M}
print(Set)