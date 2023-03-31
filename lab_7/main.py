# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

import Graph
import Vertex


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

graph = Graph.Graph()
"""to fill out, just keep adding neighbors an weight"""
graph.addVertex(1)
graph.addVertex(2)
graph.addVertex(3)
graph.addVertex(4)
graph.addVertex(5)
graph.addVertex(6)
graph.addVertex(7)

graph.addEdge(1, 2, 2)
graph.addEdge(1, 4, 1)
graph.addEdge(2, 4, 3)
graph.addEdge(2, 5, 10)
graph.addEdge(3, 1, 4)
graph.addEdge(3, 6, 5)
graph.addEdge(4, 3, 2)
graph.addEdge(4, 6, 8)
graph.addEdge(4, 7, 4)
graph.addEdge(4, 5, 2)
graph.addEdge(5, 7, 6)
graph.addEdge(7, 6, 1)


"""graph.vertList[1].isVisited = False
print(graph.vertList[1].isVisited)"""
test = graph.shortest_path(1)
print(test)
"""
path_list = [[None]] * 7
path_list[3] = []
path_list[3].append(4)
path_list[3].append(8)
path_list[6] = []
path_list[6].append(3)
print(path_list)"""