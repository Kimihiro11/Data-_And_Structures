# -*- coding: utf-8 -*-
# @Time : 2019/12/9 16:19 
# @Author : kimihiro
# @File : leetcode_145.py 
# @Software: PyCharm

# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/

# 给定一个二叉树，返回它的 前序 中序 后序 遍历。
# 示例:
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# 输出: [3,2,1]

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = []
        self.stack = []

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # if root is None:
        #     return self.res
        # self.postorderTraversal(root.left)
        # self.postorderTraversal(root.right)
        # self.res.append(root.val)
        # return self.res
        if root is None:
            return self.res
        self.stack.append(root)
        while self.stack:
            cur = self.stack.pop()
            self.res.append(cur.val)
            if cur.left:
                self.stack.append(cur.left)
            if cur.right:
                self.stack.append(cur.right)
        self.res.reverse()
        return self.res

    def preorderTraversal(self, root: TreeNode):
        if root is None:
            return self.res
        self.stack.append(root)
        while self.stack:
            cur = self.stack.pop()
            self.res.append(cur.val)
            if cur.right:
                self.stack.append(cur.right)
            if cur.left:
                self.stack.append(cur.left)
        return self.res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return self.res
        curr = root
        while self.stack or curr:
            while curr:
                self.stack.append(curr)
                curr = curr.left
            curr = self.stack.pop()
            self.res.append(curr.val)
            curr = curr.right
        return self.res
