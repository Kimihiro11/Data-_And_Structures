# -*- coding: utf-8 -*-
# @Time : 2019/12/4 下午12:59 
# @Author : kimihiro
# @File : binary_search_tree.py 
# @Software: PyCharm
import random


class Node:
    __slots__ = "element", "left", "right"

    def __init__(self, element: int = None):
        self.element = element
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self._root: Node = None
        self._size: int = 0

    def get_size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size is 0

    def add_element(self, element: int):
        # if self._root.element is None:
        #     self._root = Node(element)
        #     self._size += 1
        # else:
        #     self._root = self._add_element(self._root, element)
        self._root = self._add_element(self._root, element)

    # 添加元素 （不可重复）
    def __add_element(self, node: Node, element: int):
        if node.element == element:
            return node
        if node.left is None and node.element > element:
            node.left = Node(element)
            self._size += 1
            return node
        if node.right is None and node.element < element:
            node.right = Node(element)
            self._size += 1
            return node
        if node.element > element:
            self._add_element(node.left, element)
        else:
            self._add_element(node.right, element)
        return node

    # 简易递归实现
    def _add_element(self, node: Node, element: int) -> Node:
        if not node:
            self._size += 1
            return Node(element)
        if node.element == element:
            return node
        if node.element > element:
            node.left = self._add_element(node.left, element)
        else:
            node.right = self._add_element(node.right, element)
        return node

    def contains(self, element: int) -> bool:
        return self._contains(self._root, element)

    def _contains(self, node: Node, element: int) -> bool:
        if not node:
            return False
        if node.element == element:
            return True
        if node.element > element:
            return self._contains(node.left, element)
        else:
            return self._contains(node.right, element)

    # 前序遍历
    def pre_order(self):
        self._pre_order(self._root)

    def _pre_order(self, node: Node):
        if node is None:
            return
        print(node.element)
        self._pre_order(node.left)
        self._pre_order(node.right)

    # 中序遍历
    def in_order(self):
        self._pre_order(self._root)

    def _in_order(self, node: Node):
        if node is None:
            return
        self._pre_order(node.left)
        print(node.element)
        self._pre_order(node.right)

    # 后序遍历
    def post_order(self):
        self._pre_order(self._root)

    def _post_order(self, node: Node):
        if node is None:
            return
        self._pre_order(node.left)
        self._pre_order(node.right)
        print(node.element)

    # 非递归前序遍历
    def pre_order_nr(self):
        if not self._root:
            return
        # 使用数组的append 和pop  模拟stack结构
        stack = [self._root]
        while stack:
            cur = stack.pop()
            print(cur.element)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

    # 层序遍历 广度遍历
    def level_order(self):
        if not self._root:
            return
        # 使用数组模拟队列
        queue = [self._root]
        while queue:
            cur = queue.pop(0)
            print(cur.element)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

    # 取最小值
    def minimum(self) -> int:
        if not self._root:
            raise IndexError("BST is empty")
        return self._minimum(self._root).element

    def _minimum(self, node: Node) -> Node:
        if not node.left:
            return node
        self._minimum(node.left)

    # 取最大值
    def maximum(self) -> int:
        if not self._root:
            raise IndexError("BST is empty")
        return self._maximum(self._root).element

    def _maximum(self, node: Node) -> Node:
        if not node.right:
            return node
        self._minimum(node.right)

    # 删除最小值
    def remove_minimum(self):
        res = self.minimum()
        self._root = self._remove_minimum(self._root)
        return res

    def _remove_minimum(self, node: Node):
        if not node.left:
            right_node = node.right
            node.right = None
            self._size -= 1
            return right_node
        node.left = self._remove_minimum(node.left)
        return node

    # 删除最大值
    def remove_maximum(self) -> int:
        res = self.maximum()
        self._root = self._remove_maximum(self._root)
        return res

    def _remove_maximum(self, node: Node) -> Node:
        if not node.right:
            left_node = node.left
            node.left = None
            self._size -= 1
            return left_node
        node.right = self._remove_maximum(node.right)
        return node

    def remove(self, element: int):
        self._root = self._remove(self._root, element)

    def _remove(self, node: Node, element: int) -> Node:
        if not node:
            return node
        if node.element > element:
            node.left = self._remove(node.left, element)
            return node
        elif node.element < element:
            node.right = self._remove(node.right, element)
            return node
        else:
            if not node.left:
                r_node = node.right
                node.right = None
                self._size -= 1
                return r_node
            if not node.right:
                l_node = node.left
                node.left = None
                self._size -= 1
                return l_node
            rep_node = self._minimum(node.right)
            rep_node.right = self._remove_minimum(node.right)
            rep_node.left = node.left
            node.left, node.right = Node
            return rep_node

    def __str__(self):
        return "".join(self._gen_bst_string(self._root, 0))

    def _gen_bst_string(self, node: Node, depth: int, res=None):
        if res is None:
            res = []
        if node is None:
            res.append(self._gen_bst_depth_str(depth) + 'None\n')
            return
        res.append(self._gen_bst_depth_str(depth) + str(node.element) + 'None\n')
        self._gen_bst_string(node.left, depth + 1, res)
        self._gen_bst_string(node.right, depth + 1, res)
        return res

    def _gen_bst_depth_str(self, depth: int):
        res = ""
        for i in range(depth):
            res += "--"
        return res


if __name__ == "__main__":
    b = BST()

    for i in range(7):
        a = random.randint(0, 99)
        b.add_element(i)
    print(b)
    # print(b.contains(5))
    b.pre_order()
    print("============")
    # b.pre_order_nr()
    # print("============")
    # b.level_order()
    b.remove(4)
    print(b)
