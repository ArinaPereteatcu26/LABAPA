import time
import matplotlib.pyplot as plt
import pandas as pd
from Lab3 import GraphDFS, GraphBFS
from networkx.generators.random_graphs import erdos_renyi_graph


def run_experiment(algorithm, values):
    times = []
    for i in values:
        g = erdos_renyi_graph(i, 0.5)
        graph = algorithm()
        for a in g.edges:
            n, e = a
            graph.add_edge(n, e)
        start = time.perf_counter()
        if isinstance(graph, GraphDFS):
            graph.dfs(0)
        else:
            graph.bfs(0)
        end = time.perf_counter()
        times.append(end - start)
    return times


def plot_results(values, time_dfs, time_bfs):
    plt.plot(values, time_dfs, label="Depth First Search")
    plt.plot(values, time_bfs, label="Breadth First Search")
    plt.xlabel('Number of nodes')
    plt.ylabel('Time (seconds)')
    plt.title('Graph Traversal Algorithms')
    plt.legend()
    plt.show()


def display_results(values, time_dfs, time_bfs):
    data = []
    for i in range(len(values)):
        n = values[i]
        data.append([n, time_dfs[i], time_bfs[i]])

    headers = ["Input Size", 'DFS', 'BFS']
    df = pd.DataFrame(data, columns=headers)
    print(df)


def main():
    values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 130, 140, 150]

    time_dfs = run_experiment(GraphDFS, values)
    time_bfs = run_experiment(GraphBFS, values)

    plot_results(values, time_dfs, time_bfs)
    display_results(values, time_dfs, time_bfs)


if __name__ == "__main__":
    main()
