import self

import queue_linked_list


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.data = 0
        self.parent = None
        "self.height = -1"


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.inorderList = queue_linked_list.QueueLinkedList(10)

    def findKey(self, key):
        if self.is_empty():
            return None
        return self.findKeyHelper(self.root, key)

    def findKeyHelper(self, Node, key):
        if Node.key == key:
            return key
        elif key < Node.key:
            if Node.left is not None:
                return self.findKeyHelper(Node.left, key)
            else:
                return None
        elif key > Node.key:
            if Node.right is not None:
                return self.findKeyHelper(Node.right, key)
            else:
                return None
        else:
            return None

    def findMin(self):
        if self.root is None:
            return False
        pointer = self.root
        while pointer.left is not None:
            pointer = pointer.left
        return pointer.key

    def findMax(self):
        if self.root is None:
            return False
        pointer = self.root
        while pointer.right is not None:
            pointer = pointer.right
        return pointer.key

    def insert(self, newKey):
        newItem = TreeNode(newKey)
        if self.is_empty():
            self.root = newItem
            return newKey
        """
        if self.findKey(newKey) is not None:
            return None"""
        return self.insertHelper(self.root, newItem)

    def insertHelper(self, Node, newNode):
        if newNode.key < Node.key:
            if Node.left is not None:
                newNode.data += 1
                return self.insertHelper(Node.left, newNode)
            else:
                Node.left = newNode
                newNode.parent = Node
                newNode.data += 1
                self.size += 1
                return newNode.key
        elif newNode.key > Node.key:
            if Node.right is not None:
                newNode.data += 1
                return self.insertHelper(Node.right, newNode)
            else:
                Node.right = newNode
                newNode.parent = Node
                newNode.data += 1
                self.size += 1
                return newNode.key
        else:
            return None

    """use helper to check for element first, once find, return node, 
    use another helper for removing and updating tree"""

    def delete(self, key):
        if self.is_empty() or self.findKey(key) is None:
            return None
        return self.deleteHelper(self.root, key)

    def deleteHelper(self, Node, key):
        if Node is None:
            return None
        if key < Node.key:
            return self.deleteHelper(Node.left, key)
        elif key > Node.key:
            return self.deleteHelper(Node.right, key)
        else:
            if Node.left is None:
                rightChild = Node.right
                Node = None
                return key
            elif Node.right is None:
                leftChild = Node.left
                Node = None
                return key
            else:
                tmp = self.findMinimum(Node.right)
                Node.key = tmp.key
                Node.data = tmp.data
                Node.left = self.deleteHelper(Node.left, tmp.key)



    def findMinimum(self, Node):
        current = Node.left
        while current is not None:
            current = current.left
        return current

    def printTree(self):
        if self.is_empty():
            return None
        print("Print Tree: ")
        self.printTreeHelper(self.root)

    def printTreeHelper(self, Node):
        if Node is None:
            return
        self.printTreeHelper(Node.left)
        print(Node.key)
        self.printTreeHelper(Node.right)

    def is_empty(self):
        if self.root is None:
            return True
        return False

    """print from self, same as print tree"""

    def inorder_print_tree(self):
        print("Print InOrder Tree: ")
        self.printTree()

        """print out nodes"""

    def print_levels(self):
        if self.is_empty():
            return None
        print("Print Levels: ")
        return self.print_levels_helper(self.root)

    def print_levels_helper(self, Node):
        if Node is None:
            return
        keyValuePairs = [Node.key, Node.data]
        print(keyValuePairs)
        self.print_levels_helper(Node.left)
        self.print_levels_helper(Node.right)
