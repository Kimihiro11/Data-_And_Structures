# -*- coding: utf-8 -*-
# @Time : 2019/11/20 下午10:41 
# @Author : kimihiro
# @File : Stack.py 
# @Software: PyCharm
from typing import Any

from Array import Array
from StackAndQueue.stack.I_Stack import IStack


class Stack(IStack):
    def __init__(self, capacity: int = 10):
        self.array = Array(capacity)

    def get_size(self) -> int:
        return self.array.get_size()

    def is_empty(self) -> bool:
        return self.array.is_arr_empty()

    def pop(self) -> Any:
        return self.array.remove_last_element()

    def push(self, element: Any):
        return self.array.add_last_element(element)

    def peek(self) -> Any:
        return self.array.get_last_element()


if __name__ == "__main__":
    a = Stack()
