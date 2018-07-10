#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/7/10

class TreeNode(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def image_tree(root):
    if root is None:
        return
    root.right, root.left = root.left, root.right
    image_tree(root.left)
    image_tree(root.right)

def list_tree(node):
    while not node.value or not node.left or not node.right:
        print(node.value)


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.right = node6




