# -*- coding: utf-8 -*-
# @Time : 2019/12/2 下午4:13 
# @Author : kimihiro
# @File : LinkedQueue.py 
# @Software: PyCharm
from typing import Any

from LinkedList.I_Queue import IQueue
from LinkedList.Linked_List import Node


class LinkedQueue(IQueue):
    def __init__(self):
        self._size = 0
        self._head = Node()
        self._tail = Node()

    def is_empty(self) -> bool:
        return bool(self._size)

    def enqueue(self, element: Any):
        if self._tail.element is None:
            self._tail = Node(element)
            self._head = self._tail
        else:
            self._tail.next = Node(element)
            self._tail = self._tail.next
        self._size += 1

    def dequeue(self) -> Any:
        if not self.is_empty():
            raise ValueError("LinkedQueue is empty")
        ret = self._head
        self._head = ret.next
        ret.next = None
        if (self._head is None):
            self._tail = None
        self._size -= 1
        return ret.element

    def get_front(self) -> Any:
        if not (self.is_empty()):
            raise ValueError("LinkedQueue is empty")
        return self._head.element

    def get_size(self) -> int:
        return self._size

    def __str__(self):
        res = "Queue :front"
        res_l = []
        cur = self._head
        while cur is not None:
            res_l.append((str(cur) + '->'))
            cur = cur.next
        res = res + "".join(res_l) + "None tail"
        return res


if __name__ == "__main__":
    lq = LinkedQueue()
    for i in range(0, 10):
        lq.enqueue(i)
        print(lq)
    for i in range(0, 10):
        lq.dequeue()
        print(lq)
