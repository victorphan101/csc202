# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import Huffman_Tree


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def Huffman_decode(encoded_message):
    """use ascii to figure out character and pair with freq values
    create priority queue
    convert to nodes and make tree
    assign binary numbers to tree
    form dictionary to store binary with character
    use body to decode into original string"""
    # binary number to determine direction of tree -> adding edge

    """Loop through message and add ascii value and freq"""
    """dictionary -> freq: character"""
    char_list = {}
    index = 0
    while encoded_message[index] != '\n':
        ascii_value = ''
        while encoded_message[index] != " ":
            ascii_value += encoded_message[index]
            index += 1
        # to look at frequency number
        index += 1
        ascii_value = int(ascii_value)
        char_list[int(encoded_message[index])] = str(chr(ascii_value))
        index += 2

    """Store in queue and sort"""
    char_queue = []
    for char in char_list:
        char_queue.append((char, char_list[char]))
    char_queue.sort()

    """Translate to Huffman Tree"""
    huffmanTree = Huffman_Tree.Huffman_tree()
    while len(char_queue) > 1:
        if char_queue[0][0] < char_queue[1][0]:
            newNode = huffmanTree.insert(char_queue[0][0], char_queue[0][1], char_queue[1][0],
                                         char_queue[1][1])
        else:
            newNode = huffmanTree.insert(char_queue[1][0], char_queue[1][1], char_queue[0][0],
                                         char_queue[0][1])
        char_queue.pop(0)
        char_queue.pop(0)
        char_queue.insert(0, (newNode.freq, ''))

    """read through body of encoded message and use dictionary to decode"""
    position = encoded_message.index('\n') + 2
    decoded_message = ''
    currNode = huffmanTree.root
    while position < len(encoded_message):
        if currNode.left is None and currNode.right is None:
            decoded_message += currNode.char
            currNode = huffmanTree.root
        if encoded_message[position] == '0':
            currNode = currNode.left
        else:
            currNode = currNode.right
        position += 1

    return decoded_message


Huffman_decode("65 3 66 1 67 4 68 2 \n 1110001011111000101")

