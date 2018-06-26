#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/6/25


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def node_recurse1(head):
    """就地反转"""
    if head is None or head.next is None:
        return head
    p = head          # p是头结点
    q = head.next     # q是
    head.next = None  # 头结点的next 置空

    while q:          # 当前节点不为空
        r = q.next
        q.next = p    # 当前节点的下一个节点付给tmp
        p = q
        q = r
    return p

# 遍历并打印单链表
def list_node(node):
    while node:
        print(node.val)
        node = node.next

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5


list_node(n1)
head = node_recurse1(n1)
list_node(head)

