from unittest import TestCase

import BinHeap


class TestBinHeap(TestCase):
    def test_size_zero(self):
        newHeap = BinHeap.BinHeap(5)
        self.assertEqual(newHeap.size(), 0)

    def test_size(self):
        newHeap = BinHeap.BinHeap(5)
        newHeap.insert(25)
        newHeap.insert(15)
        newHeap.insert(75)
        newHeap.insert(45)
        newHeap.insert(23)
        newHeap.insert(81)
        self.assertEqual(newHeap.size(), 6)

    def test_is_full_true(self):
        newHeap = BinHeap.BinHeap(2)
        newHeap.insert(25)
        newHeap.insert(15)
        self.assertEqual(newHeap.is_full(), True)

    def test_is_full_false(self):
        newHeap = BinHeap.BinHeap(5)
        newHeap.insert(25)
        newHeap.insert(15)
        self.assertEqual(newHeap.is_full(), False)

    def test_is_empty(self):
        newHeap = BinHeap.BinHeap(5)
        self.assertEqual(newHeap.is_Empty(), True)

    def test_is_empty_false(self):
        newHeap = BinHeap.BinHeap(5)
        newHeap.insert(25)
        newHeap.insert(15)
        self.assertEqual(newHeap.is_Empty(), False)

    def test_resize_array(self):
        newHeap = BinHeap.BinHeap(3)
        newHeap.insert(25)
        newHeap.insert(23)
        self.assertEqual(newHeap.resizeArray(), 6)

    def test__string__(self):
        newHeap = BinHeap.BinHeap(5)
        newHeap.insert(25)
        newHeap.insert(23)
        newHeap.insert(15)
        newHeap.insert(81)
        newHeap.insert(61)
        self.assertEqual(newHeap._string_(), "15 25 23 81 61 ")

    def test__string__resize(self):
        newHeap = BinHeap.BinHeap(2)
        newHeap.insert(25)
        newHeap.insert(23)
        newHeap.insert(15)
        newHeap.insert(81)
        self.assertEqual(newHeap._string_(), "15 25 23 81 ")

    def test_insert(self):
        newHeap = BinHeap.BinHeap(3)
        newHeap.insert(25)
        newHeap.insert(23)
        newHeap.insert(15)
        newHeap.insert(81)
        newHeap.insert(61)
        self.assertEqual(newHeap.insert(20), 20)

    def test_delete_min(self):
        newHeap = BinHeap.BinHeap(5)
        newHeap.insert(25)
        newHeap.insert(23)
        newHeap.insert(15)
        newHeap.insert(81)
        newHeap.insert(61)
        self.assertEqual(newHeap.deleteMin(), 25)

    def test_delete_min_exception(self):
        newHeap = BinHeap.BinHeap(5)
        with self.assertRaises(BinHeap.MyException):
            newHeap.deleteMin()

