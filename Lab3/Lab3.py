from collections import defaultdict, deque


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
        self.dfs_util(v, visited)


class GraphBFS:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def show(self):
        for key, value in self.adj_list.items():
            print(key, "   ", value)

    def bfs(self, start_node):
        queue = deque()
        max_node = max(self.adj_list.keys(), default=-1)
        visited = [False] * (max_node + 1)

        visited[start_node] = True
        queue.append(start_node)

        while queue:
            current_node = queue.popleft()
            for neighbor in self.adj_list[current_node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
