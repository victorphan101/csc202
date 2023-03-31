import os
from unittest import TestCase

import huffman


class Test(TestCase):
    def test_cnt_freq_file_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            huffman.cnt_freq("does_not_exist.txt")

    def test_cnt_freq_one_letter(self):
        solution_array = [0] * 256
        solution_array[ord('a')] = 10
        self.assertEqual(huffman.cnt_freq("one_letter_string.txt"), solution_array)

    def test_cnt_freq_mult_ordered(self):
        solution_array = [0] * 256
        solution_array[ord('a')] = 3
        solution_array[ord('b')] = 4
        solution_array[ord('s')] = 4
        solution_array[ord('u')] = 5
        self.assertEqual(huffman.cnt_freq("mult_ordered_string.txt"), solution_array)

    def test_cnt_freq_mixed_ordered(self):
        solution_array = [0] * 256
        solution_array[ord('a')] = 5
        solution_array[ord('f')] = 2
        solution_array[ord('j')] = 6
        solution_array[ord('s')] = 5
        solution_array[ord('l')] = 3
        self.assertEqual(huffman.cnt_freq("mixed_ordered_string.txt"), solution_array)

    def test_comes_before_freq_true(self):
        freq_list = huffman.cnt_freq("standard_example.txt")
        self.assertEqual(huffman.comes_before(freq_list, 'B', 'D'), True)

    def test_comes_before_freq_false(self):
        freq_list = huffman.cnt_freq("standard_example.txt")
        self.assertEqual(huffman.comes_before(freq_list, 'A', 'E'), False)

    def test_create_huff_tree_empty_file(self):
        freq_list = huffman.cnt_freq("empty_file.txt")
        self.assertEqual(huffman.create_huff_tree(freq_list), None)

    def test_create_huff_tree_one_char(self):
        freq_list = huffman.cnt_freq("one_letter_string.txt")
        actual_root = huffman.create_huff_tree(freq_list)
        expected_root = huffman.HuffmanNode('a', 10)
        self.assertEqual(actual_root.freq, expected_root.freq)
        self.assertEqual(actual_root.char, expected_root.char)

    def test_create_huff_tree(self):
        freq_list = huffman.cnt_freq("standard_example.txt")
        actual_root = huffman.create_huff_tree(freq_list)
        expected_root = huffman.HuffmanNode('', 21)
        self.assertEqual(actual_root.freq, expected_root.freq)
        self.assertEqual(actual_root.char, expected_root.char)

    def test_create_code_no_root(self):
        freq_list = huffman.cnt_freq("empty_file.txt")
        root_node = huffman.create_huff_tree(freq_list)
        self.assertEqual(huffman.create_code(root_node), None)

    def test_create_code_one_char(self):
        freq_list = huffman.cnt_freq("one_letter_string.txt")
        root_node = huffman.create_huff_tree(freq_list)
        char_code = ['']
        self.assertEqual(huffman.create_code(root_node), char_code)

    def test_create_code(self):
        freq_list = huffman.cnt_freq("standard_example.txt")
        root_node = huffman.create_huff_tree(freq_list)
        char_code = [''] * 256
        char_code[ord('A')] = "0"
        char_code[ord('B')] = "1110"
        char_code[ord('C')] = "10"
        char_code[ord('D')] = "1111"
        char_code[ord('E')] = "110"
        self.assertEqual(huffman.create_code(root_node), char_code)

    def test_create_header_none(self):
        freq_list = huffman.cnt_freq("empty_file.txt")
        self.assertEqual(huffman.create_header(freq_list), None)

    def test_create_header_one_char(self):
        freq_list = huffman.cnt_freq("one_letter_string.txt")
        self.assertEqual(huffman.create_header(freq_list), "97 10 ")

    def test_create_header(self):
        freq_list = huffman.cnt_freq("standard_example.txt")
        self.assertEqual(huffman.create_header(freq_list), "65 7 66 1 67 6 68 2 69 5 ")

    def test_huffman_encode_in_file_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            huffman.huffman_encode("does_not_exist.txt", "standard_example_soln.txt")

    def test_huffman_encode_out_file_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            huffman.huffman_encode("standard_example.txt", "does_not_exist.txt")

    def test_huffman_encode_both_file_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            huffman.huffman_encode("does_not_exist", "does_not_exist.txt")

    def test_huffman_encode_empty(self):
        huffman.huffman_encode("empty_file.txt", "empty_file.txt")
        output_file = open("empty_file.txt")
        self.assertEqual((os.stat("empty_file.txt").st_size == 0), True)
        output_file.close()

    def test_huffman_encode_one_char(self):
        huffman.huffman_encode("one_letter_string.txt", "one_letter_string_soln.txt")
        output_file = open("one_letter_string_soln.txt")
        output_text = ''
        for line in output_file:
            for character in line:
                output_text += character
        output_file.close()
        self.assertEqual(output_text, "97 10 ")

    def test_huffman_encode(self):
        huffman.huffman_encode("standard_example.txt", "standard_example_soln.txt")
        output_file = open("standard_example_soln.txt")
        output_text = ''
        for line in output_file:
            for character in line:
                output_text += character
        output_file.close()
        self.assertEqual(output_text, "65 7 66 1 67 6 68 2 69 5 \n0000000111010101010101011111111110110110110110")