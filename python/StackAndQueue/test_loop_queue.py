# -*- coding: utf-8 -*-
# @Time : 2019/11/21 15:39 
# @Author : kimihiro
# @File : test_loop_queue.py 
# @Software: PyCharm
from unittest import TestCase

from StackAndQueue import LoopQueue


class TestLoopQueue(TestCase):
    def test_enqueue(self):
        lq = LoopQueue.LoopQueue()
        for i in range(100):
            lq.enqueue(i)
        assert lq.get_size() == 100
        assert lq.get_front() == 0

    def test_dequeue(self):
        lq = LoopQueue.LoopQueue()
        for i in range(100):
            lq.enqueue(i)
        lq.dequeue()
        assert lq.get_size() == 99
        assert lq.get_front() == 1
