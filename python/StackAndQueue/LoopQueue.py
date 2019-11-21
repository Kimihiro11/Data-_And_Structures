# -*- coding: utf-8 -*-
# @Time : 2019/11/21 上午9:32 
# @Author : kimihiro
# @File : LoopQueue.py 
# @Software: PyCharm
from StackAndQueue.I_Queue import IQueue


class LoopQueue(IQueue):
    def __init__(self, capacity: int):
        self._data = [None] * capacity
        self.front = 0
        self.tail = 0
        self._size = 0
