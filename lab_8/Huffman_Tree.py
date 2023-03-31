class Node:
    def __init__(self, character='', frequency=0):
        self.left = None
        self.right = None
        self.freq = frequency
        self.char = character
        self.code = ''
        self.height = 0


class Huffman_tree:
    def __init__(self):
        self.root = None

    def insert(self, leftFreq, leftChar, rightFreq, rightChar):
        leftNode = Node(leftChar, leftFreq)
        rightNode = Node(rightChar, rightFreq)
        if self.root is not None:
            checkRoot = self.root
            if leftFreq == checkRoot.freq and leftChar == checkRoot.char:
                leftNode = self.root
            if rightFreq == checkRoot.freq and rightChar == checkRoot.char:
                rightNode = self.root

        newNode = Node('', leftFreq + rightFreq)

        newNode.left = leftNode
        newNode.right = rightNode

        leftNode.code = '0'
        rightNode.code = '1'

        self.root = newNode
        return newNode
