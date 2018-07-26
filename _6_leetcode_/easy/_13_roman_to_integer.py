# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _13_roman_to_integer
   Description :
   Author :       Sam Yong
   date：          2018/7/24
-------------------------------------------------
   Change Activity:
                   2018/7/24:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

import unittest

class Solution_my:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900,
        }

        temp = s[:]
        sum_value = 0
        while temp != None and len(temp) != 0:

            buffer_list = list(temp)
            if (len(buffer_list) > 2) and (buffer_list[0] == buffer_list[1] == buffer_list[2]):
                sum_value += value[buffer_list[0]] * 3
                temp = temp[3:]
                continue

            elif (len(buffer_list) > 1):
                headstr = temp[:2]
                if (buffer_list[0] == buffer_list[1]):
                    sum_value += value[buffer_list[0]] * 2
                    temp = temp[2:]
                    continue

                elif (headstr in value):
                    sum_value += value[headstr]
                    temp = temp[2:]
                else:
                    sum_value += value[temp[:1]]
                    temp = temp[1:]
            else:
                sum_value += value[temp[0]]
                temp = None


        return sum_value



class Solution_EAFP():
    # EAFP : Easier to ask for forgiveness than permission (https://docs.python.org/3.5/glossary.html#term-eafp)
    # https://leetcode.com/problems/roman-to-integer/discuss/6542/4-lines-in-Python
    def romanToInt(self, s):
        value_dict = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900,
        }

        result, i = 0, 0
        while i < len(s):
            try:
                result += value_dict[s[i] + s[i+1]]  # 遍历整个list的index
                i += 2
            except (KeyError, IndexError):
                result += value_dict[s[i]]
                i += 1
        return result


class Solution():
    def romanToInt(self, s):
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        z = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]

        return z + roman[s[-1]]  # 最后一个值肯定是加，之前的值只要是前面比后面大，就需要减




class TestSolution(unittest.TestCase):
    def test_romanToInt(self):
        s = Solution()

        self.assertEqual(s.romanToInt('III'), 3, '3 is not right')
        self.assertEqual(s.romanToInt('IV'), 4, '4 is not right')
        self.assertEqual(s.romanToInt('IX'), 9, '9 is not right')
        self.assertEqual(s.romanToInt('LVIII'), 58, '58 is not right')
        self.assertEqual(s.romanToInt('MCMXCIV'), 1994, '1994 is not right')



if __name__ == '__main__':
    unittest.main()


