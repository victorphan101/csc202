# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import binarySearchTree


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

newTree = binarySearchTree.BinarySearchTree()
newTree.insert(24)
newTree.insert(35)
newTree.insert(10)
newTree.insert(15)
newTree.insert(25)
newTree.insert(23)
newTree.printTree()
newTree.inorder_print_tree()
newTree.print_levels()
print("Hello")
