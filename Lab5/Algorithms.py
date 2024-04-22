import random

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = {}
        self.graph[u][v] = w


class Algorithms:
    def kruskal(self, graph):
        result = []
        graph_edges = self.get_edges(graph)
        graph_edges.sort(key=lambda x: x[2])  # Sort edges by weight
        parent = {node: node for node in graph}

        for u, v, w in graph_edges:
            if self.find(parent, u) != self.find(parent, v):
                result.append([u, v, w])
                self.union(parent, u, v)
                return result