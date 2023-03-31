# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import BinHeap


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

newHeap = BinHeap.BinHeap(3)
newHeap.insert(25)
newHeap.insert(23)
newHeap.insert(15)
newHeap.deleteMin()
"""
newHeap.insert(81)
newHeap.insert(61)
"""
"""
newHeap.deleteMin()
print(newHeap._string_())"""