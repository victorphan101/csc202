from unittest import TestCase

import binarySearchTree
import queue_linked_list


class TestBinarySearchTree(TestCase):
    def test_find_key_true(self):
        newTree = binarySearchTree.BinarySearchTree()
        newTree.insert(22)
        newTree.insert(35)
        self.assertEqual(newTree.findKey(35), 35)

    def test_find_key_false(self):
        newTree = binarySearchTree.BinarySearchTree()
        newTree.insert(24)
        newTree.insert(35)
        newTree.insert(10)
        newTree.insert(15)
        self.assertEqual(newTree.findKey(30), None)

    def test_find_key_empty(self):
        newTree = binarySearchTree.BinarySearchTree()
        self.assertEqual(newTree.findKey(30), None)

    def test_find_min(self):
        newTree = binarySearchTree.BinarySearchTree()
        newTree.insert(24)
        newTree.insert(35)
        newTree.insert(10)
        newTree.insert(15)
        self.assertEqual(newTree.findMin(), 10)

    def test_find_max(self):
        newTree = binarySearchTree.BinarySearchTree()
        newTree.insert(24)
        newTree.insert(35)
        newTree.insert(10)
        newTree.insert(15)
        self.assertEqual(newTree.findMax(), 35)

    def test_insert(self):
        newTree = binarySearchTree.BinarySearchTree()
        self.assertEqual(newTree.insert(35), 35)

    def test_insert_multiple(self):
        newTree = binarySearchTree.BinarySearchTree()
        newTree.insert(22)
        newTree.insert(15)
        newTree.insert(35)
        self.assertEqual(newTree.insert(25), 25)

    def test_insert_duplicate(self):
        newTree = binarySearchTree.BinarySearchTree()
        newTree.insert(35)
        self.assertEqual(newTree.insert(35), None)

    def test_delete(self):
        newTree = binarySearchTree.BinarySearchTree()
        newTree.insert(24)
        newTree.insert(35)
        newTree.insert(10)
        newTree.insert(15)
        self.assertEqual(newTree.delete(15), 15)

    def test_delete_empty(self):
        newTree = binarySearchTree.BinarySearchTree()
        self.assertEqual(newTree.delete(35), None)

    def test_is_empty_true(self):
        newTree = binarySearchTree.BinarySearchTree()
        self.assertEqual(newTree.is_empty(), True)

    def test_is_empty_false(self):
        newTree = binarySearchTree.BinarySearchTree()
        newTree.insert(23)
        self.assertEqual(newTree.is_empty(), False)

    def test_inorder_print_tree_empty(self):
        newTree = binarySearchTree.BinarySearchTree()
        self.assertEqual(newTree.inorder_print_tree(), None)

    def test_print_levels_empty(self):
        newTree = binarySearchTree.BinarySearchTree()
        self.assertEqual(newTree.inorder_print_tree(), None)
