#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import random
import logging
import time

logging.basicConfig(level=logging.INFO)


class BinaryTree(object):
    """二叉查找树"""

    def __init__(self, data):
        self._data = data

        self._parent = None
        self._left_child = None
        self._right_child = None

        self._repeat = 1

    def insert(self, tree):
        if tree.data > self.data:
            if not self.right_child:
                self.right_child = tree
                tree.parent = self
            else:
                self.right_child.insert(tree)
        elif tree.data < self.data:
            if not self.left_child:
                self.left_child = tree
                tree.parent = self
            else:
                self.left_child.insert(tree)
        else:
            self._repeat += 1

    def find(self, value):
        if value > self.data:
            if not self.right_child:
                return None
            return self.right_child.find(value)
        elif value < self.data:
            if not self.left_child:
                return None
            return self.left_child.find(value)
        elif value == self.data:
            return self

    def find_min(self):
        if self.left_child:
            return self.left_child.find_min()
        else:
            return self

    def find_max(self):
        if self.right_child:
            return self.right_child.find_max()
        else:
            return self

    def height(self):
        if not self.left_child:
            left_height = 0
        else:
            left_height = self.left_child.height()

        if not self.right_child:
            right_height = 0
        else:
            right_height = self.right_child.height()

        return max(left_height, right_height) + 1

    def delete(self, value):
        """删除value，返回删除后的新树"""

        if value > self.data:
            if not self.right_child:
                raise ValueError("There isn't %s in this tree" % value)
            else:
                self.right_child.delete(value)
        elif value < self.data:
            if not self.left_child:
                raise ValueError("There isn't %s in this tree" % value)
            else:
                self.left_child.delete(value)
        else:
            # 找到待删除节点
            if self.left_child and self.right_child:
                min_right_child = self.right_child.find_min()
                self._data = min_right_child.data
                self.right_child.delete(min_right_child.data)
                # self._replace(min_right_child)
            elif self.left_child:
                self._delete_one_child(self.left_child)
            elif self.right_child:
                self._delete_one_child(self.right_child)
            else:
                # 无子节点, 删除节点, 父节点指向空
                if self.parent.left_child is self:
                    self.parent.left_child = None
                else:
                    self.parent.right_child = None

    def _delete_one_child(self, tree):
        """当前节点有一个子节点时删除操作

        :param tree: 当前节点的子节点
        :return:
        """

        # 当前节点是根
        if not self.parent:
            self.left_child = tree.left_child
            self.right_child = tree.right_child
            self._data = tree.data
            if tree.left_child:
                tree.left_child.parent = self
            if tree.right_child:
                tree.right_child.parent = self
            return

        # 当前节点是一般节点
        if self.parent.left_child is self:
            self.parent.left_child = tree
        else:
            self.parent.right_child = tree

        tree.parent = self.parent

    def _replace(self, tree):
        """替换当前节点

        :param tree: 当前节点的右儿子的最小值
        :return:
        """

        # 当前节点是根
        if not self.parent:
            tree.left_child = self.left_child
            tree.right_child = self.right_child
            tree.parent = self.parent
            self.left_child.parent = tree
            self.right_child.parent = tree
            return

        # 当前节点是一般节点
        if self.parent.left_child is self:
            self.parent.left_child = tree
        else:
            self.parent.right_child = tree
        tree.left_child = self.left_child
        tree.right_child = self.right_child
        tree.parent = self.parent
        if self.left_child:
            self.left_child.parent = tree
        if self.right_child:
            self.right_child.parent = tree

    def copy(self, tree):
        self._data = tree.data
        self.right_child = tree.right_child
        self.left_child = tree.left_child
        self.parent = tree.parent
        self._repeat = self.repeat

    @property
    def data(self):
        return self._data

    @property
    def left_child(self):
        return self._left_child

    @left_child.setter
    def left_child(self, value):
        self._left_child = value

    @property
    def right_child(self):
        return self._right_child

    @right_child.setter
    def right_child(self, value):
        self._right_child = value

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @property
    def repeat(self):
        return self._repeat


if __name__ == "__main__":
    logging.info(time.time())
    random_list = []

    insert_list = [random.choice(range(0, 100000)) for i in range(0, 100)]

    root = BinaryTree(insert_list.pop(0))
    for index, item in enumerate(insert_list):
        root.insert(BinaryTree(item))

    logging.info(time.time())

    if root.left_child:
        logging.info("left: %s " % root.left_child.height())
    if root.right_child:
        logging.info("right: %s" % root.right_child.height())
    logging.info("=====================")

    for i in range(0, 200000):
        random_integer = random.choice(range(0, 100000))
        root.insert(BinaryTree(random_integer))
        insert_list.append(random_integer)
        try:
            delete_integer = random.choice(insert_list)
            root.delete(delete_integer)
            insert_list.remove(delete_integer)
        except ValueError:
            pass
    if root and root.left_child:
        logging.info("left: %s " % root.left_child.height())
    if root and root.right_child:
        logging.info("right: %s" % root.right_child.height())

    a = 1