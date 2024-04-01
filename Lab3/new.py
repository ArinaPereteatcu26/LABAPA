import time
import matplotlib.pyplot as plt
import pandas as pd
from networkx.generators.random_graphs import erdos_renyi_graph
from collections import defaultdict

class GraphDFS:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        visited.add(v)
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)

    def dfs(self, v):
        visited = set()
        start_time = time.perf_counter()
        self.dfs_util(v, visited)
        end_time = time.perf_counter()
        return end_time - start_time

def run_experiment(values):
    times = []
    for i in values:
        g = erdos_renyi_graph(i, 0.5)
        graph = GraphDFS()
        for a in g.edges:
            n, e = a
            graph.add_edge(n, e)
        time_dfs = graph.dfs(0)
        times.append(time_dfs)
    return times

def plot_results(values, times):
    plt.plot(values, times, marker='o', linestyle='-')
    plt.xlabel('Number of nodes')
    plt.ylabel('Time (seconds)')
    plt.title('Time taken for DFS traversal vs Number of nodes')
    plt.grid(True)
    plt.show()

def main():
    values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 130, 140, 150]
    times = run_experiment(values)
    plot_results(values, times)

if __name__ == "__main__":
    main()
