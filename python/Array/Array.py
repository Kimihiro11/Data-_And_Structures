# -*- coding: utf-8 -*-
# @Time : 2019/11/18 上午11:01 
# @Author : kimihiro
# @File : Array.py 
# @Software: PyCharm
from typing import Any


class Array:
    def __init__(self, capacity: int = 10):
        self._data = [None] * capacity
        self._size = 0

    # 获取数组容量
    def get_capacity(self) -> int:
        return len(self._data)

    # 获取数组中元素个数
    def get_size(self) -> int:
        return self._size

    # 数组判空
    def is_arr_empty(self) -> bool:
        return self._size == 0

    def _judge_index(self, index: int):
        if index < 0 | index > self._size:
            raise IndexError("invalid index, index should be in range 0 to {}".format(self._size))

    # 调整数组容量
    def _resize(self, capacity: int):
        new_arr = [None] * capacity
        for i in range(self._size):
            new_arr[i] = self._data[i]
        self._data = new_arr

    # 在index 索引处插入元素 e
    def add_element(self, index: int, element: Any):
        self._judge_index(index)
        if (self._size == len(self._data)):
            self._resize(self.get_capacity() * 2)
        _i = index + 1
        while _i < self._size:
            self._data[_i + 1] = self._data[_i]
            _i += 1
        self._data[index] = element
        self._size += 1

    def add_first_element(self, element: Any):
        self.add_element(0, element)

    def add_last_element(self, element: Any):
        self.add_element(self._size, element)

    def get_element(self, index: int) -> Any:
        self._judge_index(index)
        return self._data[index]

    def get_last_element(self) -> Any:
        return self.get_element(self._size - 1)

    def get_first_element(self) -> Any:
        return self.get_element(0)

    def set_element(self, index: int, e: Any):
        self._judge_index(index)
        self._data[index] = e

    # 判断数组中是否含有指定元素
    def judge_element_in_arr(self, element: Any) -> bool:
        a = [i for i in self._data if i == element]
        return bool(a)

    # 查找数组中元素e所在的索引，如果不存在元素e，则返回-1
    def find_elements_index_in_arr(self, element: Any) -> int:
        for i in range(self._size):
            if self._data[i] == element:
                return i
        return -1

    # 删除指定索引处元素
    def remove_element_by_index(self, index: int) -> Any:
        self._judge_index(index)
        _i = index + 1
        res = self._data[index]
        while _i < self._size:
            self._data[_i - 1] = self._data[_i]
            _i += 1
        self._size -= 1
        self._data[self._size] = None
        if self._size == int(len(self._data) / 4) & len(self._data) is not 0:
            self._resize(int(len(self._data) / 2))
        return res

    def remove_first_element(self) -> Any:
        return self.remove_element_by_index(0)

    def remove_last_element(self) -> Any:
        return self.remove_element_by_index(self._size - 1)

    def remove_element(self, element: Any):
        index = self.find_elements_index_in_arr(element)
        if index != -1:
            self.remove_element_by_index(index)

    def __str__(self):
        arr = [i for i in self._data if i is not None]
        res = """
            Array:size={0},capacity={1}\n
            {2}
        """.format(self._size, len(self._data), arr)
        return res
