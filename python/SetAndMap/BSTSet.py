# -*- coding: utf-8 -*-
# @Time : 2020/1/17 下午3:52 
# @Author : kimihiro
# @File : BSTSet.py 
# @Software: PyCharm
import time
from typing import Any

from BinarySearchTree.binary_search_tree import BST
from SetAndMap import read_files
from SetAndMap.I_Set import ISet


class BSTSet(ISet):

    def __init__(self):
        self.bst = BST()

    # 利用bst的元素不可重复的性质
    def add(self, element: Any):
        self.bst.add_element(element)

    def contains(self, elememt: Any) -> bool:
        return self.bst.contains(elememt)

    def remove(self, elememt: Any):
        self.bst.remove(elememt)

    def get_size(self) -> int:
        return self.bst.get_size()

    def is_empty(self) -> int:
        return self.bst.is_empty()


if __name__ == "__main__":
    time_now = time.time()
    res1 = read_files.read_files('src/a-tale-of-two-cities.txt')
    res2 = read_files.read_files('src/pride-and-prejudice.txt')
    print("A Tale Two Cities")
    print("Total words %d" % len(res1))
    set1 = BSTSet()
    for i in res1:
        set1.add(i)
    print("different words %d:" % set1.get_size())

    print('---')

    print('Pride adn prejudice')
    print("Total words %d" % len(res2))
    set2 = BSTSet()
    for i in res2:
        set2.add(i)
    print("different words %d:" % set2.get_size())
    print("---------")
    print("Cost time %s" % (time.time() - time_now))
