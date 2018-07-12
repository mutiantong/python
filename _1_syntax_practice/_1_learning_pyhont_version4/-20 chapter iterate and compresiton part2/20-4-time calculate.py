#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     20-4-time calculate
   Description :
   Author :      'Sam Yong'
   date：          2018/7/12
-------------------------------------------------
   Change Activity:
                   2018/7/12:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

import time
import trace

repr = 1000
repslist = range(repr)


def timer(func, *pargs, **kargs):
    start = time.clock()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = time.clock() - start
    return (elapsed, ret)


## time.time计时器
if sys.platform[:3] == 'win':
    timefunc = time.clock
else:
    timefunc = time.time

def timer(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 1000)
    trace(func, pargs, kargs)
    repslist  = range(_reps)
    start = timefunc()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timefunc() - start
    return (elapsed, ret)

## 用 timeit模块
