import stack_linked_list


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def isBalanced(input):
    openList = ["[", "{", "("]
    closeList = ["]", "}", ")"]

    charArray = stack_linked_list.StackLinkedList(len(input))
    for char in input:
        if char in openList:
            charArray.push(char)
        elif char in closeList:
            pos = closeList.index(char)
            if charArray.size() > 0 and charArray.peek() == openList[pos]:
                charArray.pop()
            else:
                return False
    if charArray.size() == 0:
        return True

    return False
