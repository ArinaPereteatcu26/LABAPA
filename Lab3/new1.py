import time
import matplotlib.pyplot as plt
from networkx.generators.random_graphs import erdos_renyi_graph
from collections import defaultdict, deque

class GraphBFS:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start_node):
        queue = deque()
        max_node = max(self.adj_list.keys(), default=-1)
        visited = [False] * (max_node + 1)

        visited[start_node] = True
        queue.append(start_node)

        start_time = time.perf_counter()

        while queue:
            current_node = queue.popleft()
            for neighbor in self.adj_list[current_node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        end_time = time.perf_counter()
        return end_time - start_time

def run_experiment(values):
    times = []
    for i in values:
        g = erdos_renyi_graph(i, 0.5)
        graph = GraphBFS()
        for a in g.edges:
            n, e = a
            graph.add_edge(n, e)
        time_bfs = graph.bfs(0)
        times.append(time_bfs)
    return times

def plot_results(values, times):
    plt.plot(values, times, marker='o', linestyle='-')
    plt.xlabel('Number of nodes')
    plt.ylabel('Time (seconds)')
    plt.title('Time taken for BFS traversal vs Number of nodes')
    plt.grid(True)
    plt.show()

def main():
    values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 130, 140, 150]
    times = run_experiment(values)
    plot_results(values, times)

if __name__ == "__main__":
    main()
