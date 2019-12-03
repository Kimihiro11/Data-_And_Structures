# -*- coding: utf-8 -*-
# @Time : 2019/12/3 下午3:48 
# @Author : kimihiro
# @File : linkedlist203.py 
# @Software: PyCharm
# 203.移除链表元素
# https://leetcode-cn.com/problems/remove-linked-list-elements/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummyHead = ListNode(None)
        dummyHead.next = head
        cur: ListNode = dummyHead
        while cur.next is not None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummyHead.next
