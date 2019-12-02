# -*- coding: utf-8 -*-
# @Time : 2019/12/2 下午3:56 
# @Author : kimihiro
# @File : LinkedStack.py 
# @Software: PyCharm
from abc import ABC
from typing import Any

from LinkedList.I_Stack import IStack
from .LinkedList import LinkedList


class LinkedStack(IStack):
    def __init__(self):
        self.lk = LinkedList()

    def push(self, element: Any):
        self.lk.add_first(element)

    def get_size(self) -> int:
        return self.lk.get_size()

    def is_empty(self) -> bool:
        return self.lk.is_empty()

    def peek(self) -> Any:
        return self.lk.get_first()

    def pop(self) -> Any:
        return self.lk.get_first()

    def __str__(self):
        return self.lk


if __name__ == "__main__":
    ls = LinkedStack()
    for i in range(0, 10):
        ls.push(i)
        print(ls)
