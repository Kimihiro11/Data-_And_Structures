# -*- coding: utf-8 -*-
# @Time : 2020/1/20 下午2:53 
# @Author : kimihiro
# @File : LinkedListMap.py 
# @Software: PyCharm
from typing import Any

from SetAndMap.I_Map import IMap


class Node:
    def __init__(self, key: Any = None, value: Any = None, next=None):
        self.key = key
        self.value = value
        self.next: Node = next

    def __str__(self):
        return str(self.key) + ":" + str(self.value)


class LinkedListMap(IMap):
    def __init__(self):
        self.dummy_head: Node = Node()
        self.size = 0

    def _get_node(self, key: Any):
        cur_node = self.dummy_head.next
        while cur_node is not None:
            if cur_node.key == key:
                return cur_node
            cur_node = cur_node.next
        return None

    def add(self, key: Any, value: Any):
        node = self._get_node(key)
        if not node:
            self.dummy_head.next = Node(key, value, self.dummy_head.next)
            self.size += 1
        else:
            node.value = value

    def contains(self, key: Any) -> bool:
        return self._get_node(key) is None

    def get(self, key) -> Any:
        node = self._get_node(key)
        if not node:
            return None
        return node.value

    def set(self, key: Any, value: Any):
        node = self._get_node(key)
        if not node:
            raise KeyError
        node.value = value

    def remove(self, key: Any):
        node = self.dummy_head
        while node.next is not None:
            if node.key.key == key:
                break
            node = node.next
        if node.next is not None:
            del_node = node.next
            node.next = del_node.next
            del_node.next = None
            self.size -= 1
        return None

    def get_size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0
