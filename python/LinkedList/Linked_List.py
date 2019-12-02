# -*- coding: utf-8 -*-
# @Time : 2019/11/29 下午1:09 
# @Author : kimihiro
# @File : Linked_List.py
# @Software: PyCharm
from typing import Any


class Node:
    def __init__(self, element: Any = None, next_node=None):
        self.element = element
        self.next: Node = next_node

    def __str__(self):
        return str(self.element)


class LinkedList:
    def __init__(self):
        self.dummy_head = Node()
        self._size = 0

    # 获取链表中Node数
    def get_size(self) -> int:
        return self._size

    # 判断链表是否为空
    def is_empty(self) -> bool:
        return self._size == 0

    # 判断参数合法性
    def _judge_index(self, index: int):
        if index < 0 or index > self._size:
            raise IndexError("invalid index ")

    # 往链表中添加元素
    def add(self, index: int, element: Any):
        self._judge_index(index)

        prev = self.dummy_head
        for i in range(0, index):
            prev = prev.next
        prev.next = Node(element, prev.next)
        self._size += 1

    def add_first(self, element: Any):
        self.add(0, element)

    def add_last(self, element: Any):
        self.add(self._size, element)

    # 获取指定索引位置的节点值
    def get(self, index: int) -> Any:
        self._judge_index(index)
        prev = self.dummy_head
        for i in range(0, index):
            prev = prev.next
        return prev.next.element

    def get_first(self) -> Any:
        return self.get(0)

    def get_last(self) -> Any:
        return self.get(self._size - 1)

    # 修改指定位置的节点元素
    def set(self, index: int, element: Any):
        self._judge_index(index)
        prev = self.dummy_head.next
        for i in range(0, index):
            prev = prev.next
        prev.element = element

    def contains(self, element: Any) -> bool:
        prev = self.dummy_head
        if not self.is_empty():
            for i in range(0, self._size):
                if prev.next.element == element:
                    return True
                prev = prev.next
        return False

    # 移除指定
    def remove(self, index: int) -> Any:
        self._judge_index(index)
        prev = self.dummy_head
        for i in range(0, index):
            prev = prev.next
        ret = prev.next
        prev.next = ret.next
        ret.next = None
        self._size -= 1
        return ret.element

    def remove_first(self) -> Any:
        return self.remove(0)

    def remove_last(self) -> Any:
        return self.remove(self._size - 1)

    def remove_element(self, element):
        prev = self.dummy_head
        for i in range(0, self._size):
            if prev.next.element == element:
                break
            prev = prev.next
        cur = prev.next
        prev.next = cur.next
        cur.next = None
        self._size -= 1

    def __str__(self):
        cur = self.dummy_head.next
        res = []
        while cur is not None:
            res.append(str(cur) + "->")
            cur = cur.next
        res.append("None")
        return "".join(res)


if __name__ == "__main__":
    lk = LinkedList()
    for i in range(0, 10):
        lk.add_first(i)
        print(lk)
