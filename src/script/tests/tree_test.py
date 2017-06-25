#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import queue
import random


class BinaryNode(object):
    """二叉树节点"""

    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

    def add_left(self, b_node):
        """添加左子树"""

        self._left = b_node

    def add_right(self, b_node):
        """添加右子树"""

        self._right = b_node

    def left_child(self):
        return self._left

    def right_child(self):
        return self._right

    def data(self):
        return self._data


root = BinaryNode("+")
dep_1_1 = BinaryNode("+")
dep_1_2 = BinaryNode("*")
dep_2_1 = BinaryNode("a")
dep_2_2 = BinaryNode("*")
dep_2_3 = BinaryNode("+")
dep_2_4 = BinaryNode("g")
dep_3_1 = BinaryNode("b")
dep_3_2 = BinaryNode("c")
dep_3_3 = BinaryNode("*")
dep_3_4 = BinaryNode("f")
dep_4_1 = BinaryNode("d")
dep_4_2 = BinaryNode("e")

root.add_left(dep_1_1)
root.add_right(dep_1_2)
dep_1_1.add_left(dep_2_1)
dep_1_1.add_right(dep_2_2)
dep_1_2.add_left(dep_2_3)
dep_1_2.add_right(dep_2_4)
dep_2_2.add_left(dep_3_1)
dep_2_2.add_right(dep_3_2)
dep_2_3.add_left(dep_3_3)
dep_2_3.add_right(dep_3_4)
dep_3_3.add_left(dep_4_1)
dep_3_3.add_right(dep_4_2)


class Node(object):
    """节点"""

    def __init__(self, data):
        self._data = data
        self._parent = None
        self._children = []

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def children(self):
        return self._children

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        if not isinstance(value, Node):
            raise ValueError("value must be Node %s has been given" % str(value))
        self._parent = value

    def add_child(self, child):
        self._children.append(child)


class Tree(object):
    def __init__(self, data):
        node = Node(data)
        self._root = node
        self._callback = None

    @property
    def root(self):
        return self._root

    def _recursive(self, cur_node):

        for child in cur_node.children:
            self._recursive(child)

        self._callback(cur_node)

    def traverse_df(self, callback):
        """深度优先遍历"""
        self._callback = callback
        self._recursive(self._root)

    def traverse_bf(self, callback):
        """广度优先遍历"""
        self._callback = callback
        q = queue.Queue()
        q.put(self._root)
        cur_node = q.get()
        while cur_node:
            for child in cur_node.children:
                q.put(child)

            self._callback(cur_node)

            if q.empty():
                break
            cur_node = q.get()

    def contains(self, callback, traverse):
        traverse(self, callback)

    def add(self, data, to_data, traverse):
        child = Node(data)

        def callback(node):
            if node.data == to_data:
                child.parent = node
                node.add_child(child)

        self.contains(callback, traverse)

        if not child.parent:
            raise Exception("%s parent does exists." % data)

    def remove(self, data, traverse):

        parent = []
        child_to_remove = []

        def callback(node):
            if node.data == data:
                parent.append(node.parent)
                parent[0].children.remove(node)
                child_to_remove.append(node)

        self.contains(callback, traverse)

        if not parent:
            raise Exception("do not found parent that contains %s" % data)

        return child_to_remove[0]


def traverse_middle(tree):
    """中序遍历"""

    if not tree:
        return

    traverse_middle(tree.left_child())
    print(tree.data())
    traverse_middle(tree.right_child())

    return


def traverse_post(tree):
    """后序遍历"""

    if not tree:
        return

    traverse_post(tree.left_child())
    traverse_post(tree.right_child())
    print(tree.data())

    return


def convert_post_exp_to_tree(exp_list):
    """将后续表达式转换成表达式树"""

    stack = []
    operators = ["+", "*"]
    operands = ["a", "b", "c", "d", "e", "f", "g"]

    for exp in exp_list:
        if exp in operands:
            stack.append(BinaryNode(exp))
        elif exp in operators:
            operator = BinaryNode(exp)
            operand_right = stack.pop()
            operand_left = stack.pop()
            operator.add_right(operand_right)
            operator.add_left(operand_left)
            stack.append(operator)

    return stack


"""二叉查找树例程"""


def make_empty(tree):
    """释放二叉查找树"""

    if tree is not None:
        make_empty(tree.left_child())
        make_empty(tree.right_child())
        del tree

    return


def find_node(tree, node):
    """查找指定节点"""

    if tree is None:
        return

    if tree.data() > node.data():
        return find_node(tree.left_child(), node)
    elif tree.data() < node.data():
        return find_node(tree.right_child(), node)
    else:
        return tree


def find_min(tree):
    """查找最小节点"""

    if tree is None:
        return
    elif tree.left_child() is None:
        return tree
    else:
        return find_min(tree.left_child())


def find_max(tree):
    """查找最大节点"""

    if tree is None:
        return

    while tree.right_child() is not None:
        tree = tree.right_child()

    return tree


def insert(tree, node):
    """插入节点"""

    if tree is None:
        return node
    if tree.data() > node.data():
        tree.add_left(insert(tree.left_child(), node))
    else:
        tree.add_right(insert(tree.right_child(), node))

    return tree


def delete(tree, node):
    """删除节点"""

    if tree is None:
        raise Exception("node was not found.")

    if node.data() < tree.data():
        tree.add_left(delete(tree.left_child(), node))
    elif node.data() > tree.data():
        tree.add_right(delete(tree.right_child(), node))
    else:
        if tree.left_child() and tree.right_child():
            temp_node = find_min(tree.right_child())
            tree.add_right(delete(tree.right_child(), temp_node))
            tree = temp_node
        else:
            if tree.left_child():
                tree = tree.left_child()
            elif tree.right_child():
                tree = tree.right_child()
            else:
                del tree

    return tree

exist_data = []


def add_exist_data(node):
    exist_data.append(node.data)


def main():
    seq = [i for i in range(0, 9999)]
    random_list = []
    for j in range(0, 9999):
        random_list.append(random.choice(seq))

    binary_root = insert(None, BinaryNode(random_list.pop(0)))
    for key in random_list:
        insert(binary_root, BinaryNode(key))


    binary_root.traverse_bf(add_exist_data)
    insert_list = []
    delete_list = []

    for n in range(0, 99999):
        delete_list

    delete(binary_root, BinaryNode(10))
    a = 1


if __name__ == "__main__":
    main()
