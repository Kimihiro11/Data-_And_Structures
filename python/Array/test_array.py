# -*- coding: utf-8 -*-
# @Time : 2019/11/18 下午1:36 
# @Author : kimihiro
# @File : test_array.py 
# @Software: PyCharm
import random
import unittest
from .Array import Array as Ar


class TestArray(unittest.TestCase):
    def test_add_element(self):
        a = Ar()
        for i in range(10):
            a.add_element(i, i)
        print(a._data)
        assert a._data == [i for i in range(10)]

    def test_add_element_first(self):
        a = Ar(5)
        a.add_first_element(6)
        assert a.get_element(0) == 6

    def test_add_element_end(self):
        a = Ar(20)
        for i in range(10):
            a.add_element(i, i)
        a.add_last_element(9)
        assert a.get_element(a.get_size() - 1) == 9

    def test_judge_element_in_arr(self):
        a = Ar(20)
        for i in range(20):
            a.add_element(i, i)
        res = a.judge_element_in_arr(5)
        assert res is True

    def test_find_elements_index_in_arr(self):
        a = Ar(20)
        for i in range(20):
            a.add_element(i, i)
        res = a.find_elements_index_in_arr(19)

        assert res == 19

    def test_remove_element_by_index_in_arr(self):
        a = Ar(20)
        for i in range(20):
            a.add_element(i, i)
        a.remove_element_by_index(5)
        assert a.get_element(5) == 6

    def test_remove_first_element(self):
        a = Ar(20)
        for i in range(20):
            a.add_element(i, i)
        a.remove_last_element()
        assert a.get_element(18) == 18

    def test_remove_element_in_arr(self):
        a = Ar(5)
        for i in range(5):
            a.add_element(i, i)
        a.remove_element(2)
        print(a._data)
        assert a._data == [0, 1, 3, 4, None]

    def test_print_arr(self):
        a = Ar(5)
        for i in range(5):
            a.add_element(i, i)
        print(a)
