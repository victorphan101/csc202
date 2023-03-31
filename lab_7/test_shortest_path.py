from unittest import TestCase

import Graph


class TestGraph(TestCase):
    def test_shortest_path(self):
        graph = Graph.Graph()
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

        print(graph.shortest_path(1))
