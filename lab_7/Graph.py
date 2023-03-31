import sys
from _ctypes import Array

from Vertex import Vertex


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def shortest_path(self, vertex):
        short_path_list = {}
        distance = [None] * (len(self.vertList) + 1)
        distance[vertex] = 0
        path_list = [None] * (len(self.vertList) + 1)
        path_list[vertex] = [vertex]
        """set_list = [vertex, path list, cost]"""
        for num in self.vertList:
            set_list = [num]
            queue_visited = [vertex]
            while len(queue_visited) > 0:
                u = queue_visited.pop(0)
                if path_list[u] is None:
                    path_list[u] = []
                self.vertList[u].isVisited = True

                for v in self.vertList[u].connectedTo:
                    key = v.getId()
                    if self.vertList[key].isVisited is False:
                        queue_visited.append(key)
                    weight = self.vertList[u].getWeight(self.vertList[key])
                    if distance[key] is None or distance[key] > distance[u] + weight:
                        distance[key] = distance[u] + weight
                        if path_list[key] is None:
                            path_list[key] = []
                        path_list[key] = []
                        for i in path_list[u]:
                            path_list[key].append(i)
                        path_list[key].append(key)
            set_list.append(path_list[num])
            set_list.append(distance[num])
            short_path_list[num] = set_list
        return short_path_list
