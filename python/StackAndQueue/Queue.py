# -*- coding: utf-8 -*-
# @Time : 2019/11/20 下午11:41 
# @Author : kimihiro
# @File : Queue.py 
# @Software: PyCharm
from typing import Any

from Array import Array
from StackAndQueue.I_Queue import IQueue


class Queue(IQueue):
    def __init__(self, capacity: int = 10):
        self.array = Array(capacity)

    def get_size(self) -> int:
        return self.array.get_size()

    def is_empty(self) -> bool:
        return self.array.is_arr_empty()

    def dequeue(self) -> Any:
        return self.array.remove_first_element()

    def enqueue(self, element: Any):
        self.array.add_last_element(element)

    def get_front(self) -> Any:
        return self.array.get_first_element()
