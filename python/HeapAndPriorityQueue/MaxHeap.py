# -*- coding: utf-8 -*-
# @Time : 2020/1/26 下午1:01 
# @Author : kimihiro
# @File : MaxHeap.py 
# @Software: PyCharm
import random
import time
from typing import Any


class MaxHeap:
    def __init__(self, arr: list = None):
        if arr is not None:
            self.data = arr
            i = len(self.data) - 1
            while i >= 0:
                self._shift_down(i)
                i -= 1
        else:
            self.data = []

    def size(self) -> int:
        return len(self.data)

    def isEmpty(self) -> bool:
        return len(self.data) == 0

    def _parent(self, index: int):
        """
        计算一个索引的父亲节点的索引
        :param index:
        :return:
        """
        if not index:
            raise IndexError
        return int((index - 1) / 2)

    def leftChild(self, index: int) -> int:
        # 计算一个索引的左节点
        return index * 2 + 1

    def rightChild(self, index: int) -> int:
        # 计算一个索引的右节点
        return index * 2 + 2

    @property
    def _size(self):
        return len(self.data) - 1

    def add(self, e: Any):
        self.data.append(e)
        self._shift_up(self._size)

    def _shift_up(self, k: int):
        while k > 0 and self.data[self._parent(k)] < self.data[k]:
            self._swap(k, self._parent(k))
            k = self._parent(k)

    def _swap(self, i: int, j: int):
        cur = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = cur

    def find_max(self):
        if not self.data:
            raise ValueError("No data")
        return self.data[0]

    def extract_max(self):
        """
        取出最大节点
        将data[0] 和 data[-1] 作交换后进行下沉操作
        :return:
        """
        ret = self.find_max()
        self._swap(0, self._size)
        self.data.pop(-1)
        self._shift_down(0)
        return ret

    def _shift_down(self, k: int):
        while self.leftChild(k) < len(self.data):
            j = self.leftChild(k)
            if (j + 1) < len(self.data) and self.data[j + 1] > self.data[j]:
                j += 1
            try:
                if self.data[k] >= self.data[j]:
                    break
            except:
                print(k)
                print(j)
            self._swap(k, j)
            k = j

    def replace(self, e: Any):
        ret = self.find_max()
        self.data[0] = e
        self._shift_down(0)
        return ret


if __name__ == "__main__":
    def testHeap(arr: list, is_heapify: bool):
        now = time.time()
        if is_heapify:
            maxHeap = MaxHeap(arr)
        else:
            maxHeap = MaxHeap()
            for i in arr:
                maxHeap.add(i)
        new_arr = []
        for i in range(len(arr)):
            new_arr.append(maxHeap.extract_max())
        for i in range(1, len(new_arr)):
            if new_arr[i - 1] < new_arr[i]:
                raise ValueError
        print("success")
        end = time.time()
        return end - now


    a_len = 100000
    test_data = []
    random.randrange(0, 100001)
    while len(test_data) != a_len:
        test_data.append(random.randrange(0, 100000000))

    time1 = testHeap(test_data, True)
    print(time1)
    time2 = testHeap(test_data, False)
    print(time2)
