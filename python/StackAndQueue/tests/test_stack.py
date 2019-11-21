# -*- coding: utf-8 -*-
# @Time : 2019/11/21 上午9:05 
# @Author : kimihiro
# @File : test_stack.py 
# @Software: PyCharm

from unittest import TestCase

from StackAndQueue.stack.Stack import Stack


class TestStack(TestCase):
    def test_get_size(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)
        assert stack.get_size() == 10

    def test_is_empty(self):
        stack = Stack()
        assert stack.is_empty() is True

    def test_push(self):
        stack = Stack()
        stack.push(1)
        assert stack.get_size() == 1
        assert stack.peek() == 1

    def test_pop(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)
        res = stack.pop()
        assert res == 9
        assert stack.get_size() == 9
