# -*- coding: utf-8 -*-
# @Time : 2020/1/20 上午10:19 
# @Author : kimihiro
# @File : BSTMAP.py 
# @Software: PyCharm
import time
from typing import Any

from SetAndMap import read_files
from SetAndMap.I_Map import IMap


class Node:
    def __init__(self, key: Any, value: Any):
        self.key = key
        self.value = value
        self.left: Node = None
        self.right: Node = None


class BSTMap(IMap):
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, key: Any, value: Any):
        self.root = self._add(self.root, key, value)

    def _add(self, node: Node, key: Any, value: Any):
        """
        递归 实现添加元素
        :param node:
        :param key:
        :param value:
        :return:
        """
        if node is None:
            self.size += 1
            return Node(key, value)
        if key < node.key:
            node.left = self._add(node.left, key, value)
        elif key > node.key:
            node.right = self._add(node.right, key, value)
        else:
            node.value = value
        return node

    def _get_node(self, node: Node, key: Any):
        """
        递归 找出key相等的节点
        :param node:
        :param key:
        :return:
        """
        if node is None:
            return None
        if key == node.key:
            return node
        elif key < node.key:
            return self._get_node(node.left, key)
        else:
            return self._get_node(node.right, key)

    def contains(self, key: Any) -> bool:
        return self.get(key) is not None

    def get(self, key) -> Any:
        node = self._get_node(self.root, key)
        if not node:
            return None
        return node.value

    def set(self, key: Any, value: Any):
        """更新操作"""
        node = self._get_node(self.root, key)
        if not node:
            raise KeyError("Invalid Key")
        node.value = value

    def _mini_node(self, node: Node):
        """查找最小节点"""
        if node.left is Node:
            return node
        return self._mini_node(node.left)

    def _remove_mini(self, node: Node):
        if node.left is None:
            right_node = node.right
            node.right = None
            self.size -= 1
            return right_node
        node.left = self._remove_mini(node.left)
        return node

    def remove(self, key: Any):
        node = self._get_node(self.root, key)
        if not node:
            return None
        self.root = self._remove(self.root, key)
        return node.value

    def _remove(self, node: Node, key: Any):
        # 递归终止条件
        if node is None:
            return None
        if node.key < key:
            node.left = self._remove(node.left, key)
            return node
        elif node.key > key:
            node.right = self._remove(node.right, key)
            return node
        else:
            if node.left is None:
                right_node = node.right
                self.size -= 1
                node.right = None
                return right_node
            if node.right is None:
                left_node = node.left
                self.size -= 1
                node.left = None
                return left_node
            # 依照bst的删除节点算法 右节点的最小值就是替换节点
            replace_node = self._mini_node(node.right)
            replace_node.right = self._remove_mini(node.right)
            replace_node.left = node.left
            node.left, node.right = None, None
            return replace_node

    def get_size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0


if __name__ == "__main__":
    time_now = time.time()
    res2 = read_files.read_files('src/pride-and-prejudice.txt')
    print("Pride adn prejudice")
    print("Total words %d" % len(res2))
    map1 = BSTMap()
    for i in res2:
        if map1.contains(i):
            map1.set(i, map1.get(i) + 1)
        else:
            map1.add(i, 1)
    print("different words %d:" % map1.get_size())
    print("Frequency of Pride %d" % map1.get('pride'))
    print("Frequency of Prejudice %d" % map1.get('prejudice'))
    print('---')
    print("Cost time %s" % (time.time() - time_now))

    time_now = time.time()
    print("Pride adn prejudice")
    print("Total words %d" % len(res2))
    map2 = {}
    for i in res2:
        if map2.get(i):
            map2[i] = map2[i] + 1
        else:
            map2.update({i: 1})
    print("different words %d:" % map2.__len__())
    print("Frequency of Pride %d" % map2.get('pride'))
    print("Frequency of Prejudice %d" % map2.get('prejudice'))
    print('---')
    print("Cost time %s" % (time.time() - time_now))
