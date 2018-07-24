# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _9_palindrom
   Description :
   Author :       Sam Yong
   date：          2018/7/23
-------------------------------------------------
   Change Activity:
                   2018/7/23:
-------------------------------------------------
"""
__author__ = 'Sam Yong'


def isPalindrome( x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    else:
        reservedNumber = 0
        while x > reservedNumber:
            reservedNumber = reservedNumber * 10 + x % 10
            x = x // 10

        if (x == reservedNumber) or (x == reservedNumber // 10):
            return True
        else:
            return False


if __name__ == '__main__':
    print(isPalindrome(121))