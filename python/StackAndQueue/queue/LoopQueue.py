# -*- coding: utf-8 -*-
# @Time : 2019/11/21 上午9:32 
# @Author : kimihiro
# @File : LoopQueue.py 
# @Software: PyCharm
from typing import Any

from StackAndQueue.queue.I_Queue import IQueue


class LoopQueue(IQueue):
    def __init__(self, capacity: int = 10):
        self._data = [None] * (capacity - 1)
        self._front = 0
        self._tail = 0
        self._size = 0

    # 获取容积 主动放弃一块区域的使用
    def get_capacity(self) -> int:
        return len(self._data) - 1

    def get_size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._front == self._tail

    # 扩缩容 操作
    def _resize(self, capacity: int):
        new_data = [None] * (capacity - 1)
        for i in range(len(self._data)):
            new_data[i] = self._data[(i + self._front) % len(self._data)]

        self._data = new_data
        self._front = 0
        self._tail = self._size

    # 入队
    def enqueue(self, element: Any):
        # 当对列满时扩容
        if ((self._tail + 1) % len(self._data)) == self._front:
            self._resize(self.get_capacity() * 2)

        self._data[self._tail] = element
        self._tail = (self._tail + 1) % len(self._data)
        self._size += 1

    # 出队
    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("The queue is empty")
        res = self._data[self._front]
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if (self._size == len(self._data) / 4 and self.get_capacity() / 2 is not 0):
            self._resize(int(self.get_capacity() / 2))
        return res

    def get_front(self) -> Any:
        if self.is_empty():
            raise IndexError("The queue is empty")
        res = self._data[self._front]
        return res
