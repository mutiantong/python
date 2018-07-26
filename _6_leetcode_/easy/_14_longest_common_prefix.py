# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _14_longest_common_prefix
   Description :
   Author :       Sam Yong
   date：          2018/7/25
-------------------------------------------------
   Change Activity:
                   2018/7/25:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

import unittest


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) < 1:
            return ""

        list_len = [len(x) for x in strs]
        list_len.sort()
        small = list_len[0]

        result = ""

        for i in range(small):
            cout = 0
            for element in strs:
                if element[i] == strs[0][i]:
                    cout += 1

            if cout == len(strs):
                result += strs[0][i]
            else:
                break


        return result


class TestSolution(unittest.TestCase):
    def test_longestCommonPrefix(self):
        s = Solution()
        self.assertEqual(s.longestCommonPrefix(["flower","flow","flight"]), "fl", "fl is wrong")
        self.assertEqual(s.longestCommonPrefix(["dog","racecar","car"]), "", "empty is wrong")



if __name__ == '__main__':
    unittest.main()

