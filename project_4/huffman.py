import os


def cnt_freq(filename):
    # checks if file exists
    if not os.path.isfile(filename):
        raise FileNotFoundError

    count_occurrences = [0] * 256
    file = open(filename, "r", newline="")
    for line in file:
        for character in line:
            # convert character into ASCII value
            count_occurrences[ord(character)] += 1
    file.close()
    return count_occurrences


def create_huff_tree(freq_list):
    # check if freq_list contains any zeros, if do, return None
    checkNonzero = list(filter(lambda item: item > 0, freq_list))
    if len(checkNonzero) == 0:
        return None
    # check if freq_list contains only one non-zero
    elif len(checkNonzero) == 1:
        return HuffmanNode(chr(freq_list.index(checkNonzero[0])), checkNonzero[0])

    char_queue = []
    for index in range(len(freq_list)):
        if freq_list[index] != 0:
            """adding items to queue represented as tuples: (character, freq)"""
            char_queue.append((freq_list[index], chr(index)))
    char_queue.sort()

    huffman_tree = Huffman_tree()
    while len(char_queue) > 1:
        if comes_before(freq_list, char_queue[0][1], char_queue[1][1]):
            newNode = huffman_tree.insert(char_queue[0][0], char_queue[0][1], char_queue[1][0],
                                          char_queue[1][1])
        else:
            newNode = huffman_tree.insert(char_queue[1][0], char_queue[1][1], char_queue[0][0],
                                          char_queue[0][1])
        char_queue.pop(0)
        char_queue.pop(0)
        char_queue.insert(0, (newNode.freq, ''))
    return huffman_tree.root


def comes_before(freq_list, a, b):
    if len(a) != 0 and len(b) != 0:
        if freq_list[ord(a)] == freq_list[ord(b)]:
            if ord(a) < ord(b):
                return True
        if freq_list[ord(a)] < freq_list[ord(b)]:
            return True
    return False


def create_code(root_node):
    if root_node is None:
        return None
    # if only one character used in file
    elif root_node.left is None and root_node.right is None:
        char_code = []
        char_code.append('')
        return char_code
    char_code = [''] * 256
    currCode = ''

    # Helper method for create_code
    def find_code(node, currentCode):
        currentCode += node.code
        if node.left:
            find_code(node.left, currentCode)
        if node.right:
            find_code(node.right, currentCode)
        if not node.left and not node.right:
            char_code[ord(node.char)] = currentCode

    find_code(root_node, currCode)
    return char_code


def create_header(freq_list):
    # check if freq_list contains any zeros, if do, return None
    checkNonzero = list(filter(lambda item: item > 0, freq_list))
    if len(checkNonzero) == 0:
        return None

    header = ''
    for index in range(len(freq_list)):
        if freq_list[index] != 0:
            header += str(index) + " " + str(freq_list[index]) + " "
    return header


def huffman_encode(in_file, out_file):
    # checks if file exists
    if not os.path.isfile(in_file) or not os.path.isfile(out_file):
        raise FileNotFoundError

    # checks if in_file is empty
    if os.stat(in_file).st_size == 0:
        return

    freq_list = cnt_freq(in_file)

    # Create the header
    header = create_header(freq_list)

    # Create the Tree and retrieve node
    root_node = create_huff_tree(freq_list)
    char_code = create_code(root_node)

    # Form output code for out_file
    # check if there is one character
    output_code = ""
    if len(char_code) == 1:
        output_code = header
    else:
        # Create body
        body_code = create_body(char_code, header)
        output_code = header + "\n" + body_code
    new_file = open(out_file, "w+", newline='')
    new_file.write(output_code)
    new_file.close()


# Helper method for huffman_encode
def create_body(char_code, header):
    body_code = ""
    index = 0
    while index < len(header):
        char_index = ''
        while header[index] != " ":
            char_index += header[index]
            index += 1
        index += 1
        for i in range(int(header[index])):
            body_code += char_code[int(char_index)]
        index += 2
    return body_code


class HuffmanNode:
    def __init__(self, character='', frequency=0):
        self.left = None
        self.right = None
        self.freq = frequency
        self.char = character
        self.code = ''


class Huffman_tree:
    def __init__(self):
        self.root = None

    def insert(self, leftFreq, leftChar, rightFreq, rightChar):
        leftNode = HuffmanNode(leftChar, leftFreq)
        rightNode = HuffmanNode(rightChar, rightFreq)
        if self.root is not None:
            checkRoot = self.root
            if leftFreq == checkRoot.freq and leftChar == checkRoot.char:
                leftNode = self.root
            if rightFreq == checkRoot.freq and rightChar == checkRoot.char:
                rightNode = self.root

        newNode = HuffmanNode('', leftFreq + rightFreq)

        newNode.left = leftNode
        newNode.right = rightNode

        leftNode.code = '0'
        rightNode.code = '1'

        self.root = newNode
        return newNode
