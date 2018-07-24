# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _7_reverse_integer
   Description :
   Author :       Sam Yong
   date：          2018/7/22
-------------------------------------------------
   Change Activity:
                   2018/7/22:
-------------------------------------------------
"""
__author__ = 'Sam Yong'


class Solution:
    def reverse1(self, x):
        """
        :type x: int
        :rtype: int
        """

        def get_int_size(x):
            size = 0
            while x != 0 and x != -1:
                size += 1
                x = x // 10
            return size

        if (x > (2**31 -1)) or (x < (-2**31)):
            return 0

        input_value = x
        if x < 0:
            x = -x

        size = get_int_size(x)
        sum_value = 0


        while x != 0 :
            sum_value += (x % 10) * (10 **(size -1))
            size -= 1
            x = x // 10

        if (sum_value > (2**31 -1)):
            return 0

        if input_value > 0:
            return sum_value
        else:
            return -sum_value

    def reverse(self, x):
        s = 1 if x > 0 else -1
        r = int((str(s * x))[::-1]) # 利用字符串的翻转
        return s * r * (r < 2 ** 31)



if __name__ == '__main__':
    print(101%10)
    print(1001 // 10)

    s = Solution()
    print(s.reverse(12345678))




