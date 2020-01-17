# -*- coding: utf-8 -*-
# @Time : 2020/1/17 下午4:33 
# @Author : kimihiro
# @File : LinkedListSet.py 
# @Software: PyCharm
import time
from typing import Any

from LinkedList.Linked_List import LinkedList
from SetAndMap import read_files
from SetAndMap.I_Set import ISet


class LinkedListSet(ISet):
    def __init__(self):
        self.l_list = LinkedList()

    # 添加每次添加元素都会遍历链表速度极慢
    def add(self, element: Any):
        if not self.l_list.contains(element):
            self.l_list.add_first(element)

    def contains(self, elememt: Any) -> bool:
        return self.l_list.contains(elememt)

    def remove(self, elememt: Any):
        self.l_list.remove(elememt)

    def get_size(self) -> int:
        return self.l_list.get_size()

    def is_empty(self) -> int:
        return self.l_list.is_empty()


if __name__ == "__main__":
    time_now = time.time()
    res1 = read_files.read_files('src/a-tale-of-two-cities.txt')
    res2 = read_files.read_files('src/pride-and-prejudice.txt')
    print("A Tale Two Cities")
    print("Total words %d" % len(res1))
    set1 = LinkedListSet()
    for i in res1:
        set1.add(i)
    print("different words %d:" % set1.get_size())

    print('---')

    print('Pride adn prejudice')
    print("Total words %d" % len(res2))
    set2 = LinkedListSet()
    for i in res2:
        set2.add(i)
    print("different words %d:" % set2.get_size())
    print("---------")
    print("Cost time %s" % (time.time() - time_now))
