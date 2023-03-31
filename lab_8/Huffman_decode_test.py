from unittest import TestCase

import Huffman_Tree
import main


class Huffman_decode_Test(TestCase):
    def test_huffman_tree_insert(self):
        huffmanTree = Huffman_Tree.Huffman_tree()
        new_node = huffmanTree.insert(3, 'A', 6, 'B')
        self.assertEqual(new_node.char, '')
        self.assertEqual(new_node.freq, 9)

    def test_huffman_decode_trial_1(self):
        self.assertEqual(main.Huffman_decode("65 3 66 1 67 4 68 2 \n 1110001011111000101"), "DCCCADBCCA")

    def test_huffman_decode_trial_2(self):
        self.assertEqual(main.Huffman_decode("65 5 66 3 67 2 68 4 \n 111001011010101010"), "BAADCDDD")

    def test_huffman_decode_trial_3(self):
        self.assertEqual(main.Huffman_decode("65 8 66 5 67 3 68 9 \n 001010111011001101010"), "DDAABDCDCA")
