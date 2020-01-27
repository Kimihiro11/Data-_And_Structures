# -*- coding: utf-8 -*-
# @Time : 2020/1/27 下午12:48 
# @Author : kimihiro
# @File : PriorityQueue.py 
# @Software: PyCharm
from typing import Any

from HeapAndPriorityQueue.I_Queue import IQueue
from HeapAndPriorityQueue.MaxHeap import MaxHeap


class PriorityQueue(IQueue):
    def __init__(self):
        self.max_heap = MaxHeap()

    def get_size(self) -> int:
        return self.max_heap.size()

    def is_empty(self) -> bool:
        return self.max_heap.isEmpty()

    def enqueue(self, element: Any):
        self.max_heap.add(element)

    def dequeue(self) -> Any:
        return self.max_heap.extract_max()

    def get_front(self) -> Any:
        return self.max_heap.find_max()
