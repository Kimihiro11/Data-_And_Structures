# -*- coding: utf-8 -*-
# @Time : 2019/11/21 上午9:14 
# @Author : kimihiro
# @File : test_queue.py 
# @Software: PyCharm

from unittest import TestCase

from .Queue import Queue


class TestQueue(TestCase):
    def test_get_size(self):
        queue = Queue()
        for i in range(10):
            queue.enqueue(i)
        assert queue.get_size() == 10

    def test_is_empty(self):
        queue = Queue()
        assert queue.is_empty() is True

    def test_enqueue(self):
        queue = Queue()
        for i in range(100):
            queue.enqueue(i)
        assert queue.get_size() == 100
        assert queue.get_front() == 0

    def test_dequeue(self):
        queue = Queue()
        for i in range(10):
            queue.enqueue(i)
        res = queue.dequeue()
        assert res == 0
        res2 = queue.dequeue()
        assert res2 == 1
        assert queue.get_size() == 8
