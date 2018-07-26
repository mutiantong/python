# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _2_add_two_nums
   Description :
   Author :       Sam Yong
   date：          2018/7/19
-------------------------------------------------
   Change Activity:
                   2018/7/19:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x, nextvalue = None):
        self.val = x
        self.next = nextvalue

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        buff_list_1 = []
        temp_dumy1 = l1
        while temp_dumy1 is not None:
            buff_list_1.append(temp_dumy1.val)
            temp_dumy1 = temp_dumy1.next

        buff_list_2 = []
        temp_dumy2 = l2
        while temp_dumy2 is not None:
            buff_list_2.append(temp_dumy2.val)
            temp_dumy2 = temp_dumy2.next

        buff_list_1.reverse()
        buff_list_2.reverse()

        for x in len(buff_list_1):
            pass


        print(buff_list_1)
        print(buff_list_2)




if __name__ == '__main__':
    l3 = ListNode(3)
    l2 = ListNode(2, l3)
    l1 = ListNode(1, l2)

    l_3 = ListNode(4)
    l_2 = ListNode(6, l_3)
    l_1 = ListNode(5, l_2)

    solute = Solution()
    solute.addTwoNumbers(l1, l_1)