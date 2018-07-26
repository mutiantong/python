#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     demo_1
   Description :
   Author :      'Sam Yong'
   date：          2018/7/24
-------------------------------------------------
   Change Activity:
                   2018/7/24:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('inteasea', type=int, help='display an integer')
args = parser.parse_args()

print(args.inteasea)
