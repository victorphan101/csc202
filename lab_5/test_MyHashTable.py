from unittest import TestCase

import MyHashTable


class TestMyHashTable(TestCase):
    def test_load_factor_empty(self):
        newHash = MyHashTable.MyHashTable()
        self.assertEqual(newHash.load_factor(), 0)

    def test_load_factor(self):
        newHash = MyHashTable.MyHashTable()
        newHash.insert(24, 8)
        newHash.insert(23, 6)
        self.assertEqual(newHash.load_factor(), float(2/11))

    def test_insert(self):
        newHash = MyHashTable.MyHashTable()
        newHash.insert(24, 8)
        newHash.insert(23, 6)
        self.assertEqual(newHash.insert(30, 35), 3)

    def test_insert_collision(self):
        newHash = MyHashTable.MyHashTable()
        newHash.insert(24, 8)
        newHash.insert(23, 6)
        self.assertEqual(newHash.insert(2, 35), 1)

    def test_insert_need_rehash(self):
        newHash = MyHashTable.MyHashTable()
        newHash.insert(24, 8)
        newHash.insert(23, 6)
        newHash.insert(25, 8)
        newHash.insert(26, 6)
        newHash.insert(27, 8)
        newHash.insert(28, 6)
        newHash.insert(29, 8)
        newHash.insert(33, 6)
        newHash.insert(32, 8)
        newHash.insert(30, 6)
        newHash.insert(61, 8)
        newHash.insert(81, 8)
        newHash.insert(18, 6)
        newHash.insert(16, 8)
        self.assertEqual(newHash.insert(8, 5), 5)

    def test_get_found(self):
        newHash = MyHashTable.MyHashTable()
        newHash.insert(24, 8)
        newHash.insert(23, 6)
        self.assertEqual(newHash.get(23), 6)

    def test_get_error(self):
        newHash = MyHashTable.MyHashTable()
        newHash.insert(24, 8)
        newHash.insert(23, 6)
        self.assertEqual(newHash.get(35), LookupError)

    def test_remove_error(self):
        newHash = MyHashTable.MyHashTable()
        newHash.insert(24, 8)
        newHash.insert(23, 6)
        self.assertEqual(newHash.remove(35), LookupError)

    def test_remove(self):
        newHash = MyHashTable.MyHashTable()
        newHash.insert(24, 8)
        newHash.insert(23, 6)
        newHash.insert(35, 20)
        newHash.insert(61, 23)
        self.assertEqual(newHash.remove(35), 1)
