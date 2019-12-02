# -*- coding: utf-8 -*-
# @Time : 2019/12/2 下午3:45 
# @Author : kimihiro
# @File : test_linkedlist.py 
# @Software: PyCharm
from unittest import TestCase
from LinkedList.LinkedList import LinkedList


class TestLinkedList(TestCase):
    def test_add_first(self):
        lk = LinkedList()
        for i in range(0, 10):
            lk.add_first(i)
        assert lk.get_first() == 9

    def test_remove(self):
        lk = LinkedList()
        for i in range(0, 10):
            lk.add_first(i)
        lk.remove_first()
        assert lk.get_first() == 8
        lk.remove_last()
        assert lk.get_last() == 1

    def test_set_elememt(self):
        lk = LinkedList()
        for i in range(0, 10):
            lk.add_first(i)
        assert lk.get_first() == 9
        lk.set(9, 99)
        assert lk.get_last() == 99
        lk.set(5, 788)
        assert lk.contains(788) is True
