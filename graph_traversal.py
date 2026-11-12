from collections import deque


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        """Adds an undirected edge between vertices u and v"""
        self.adj_list.setdefault(u, []).append(v)
        self.adj_list.setdefault(v, []).append(u)

    def bfs(self, start):
        """Breadth-First Search for Graph"""
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []

        while queue:
            curr = queue.popleft()
            result.append(curr)
            for neighbor in self.adj_list.get(curr, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def dfs(self, start):
        """Depth-First Search for Graph"""
        visited = set()
        result = []
        self._dfs_helper(start, visited, result)
        return result

    def _dfs_helper(self, curr, visited, result):
        visited.add(curr)
        result.append(curr)
        for neighbor in self.adj_list.get(curr, []):
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited, result)


if __name__ == "__main__":
    print("=== SECTION 2: GRAPH TRAVERSALS (BAROMAN) ===")

    # Constructing Graph with vertices: {B, A, R, O, M, N}
    graph = Graph()
    graph.add_edge('B', 'A')
    graph.add_edge('A', 'R')
    graph.add_edge('R', 'O')
    graph.add_edge('O', 'M')
    graph.add_edge('M', 'A')
    graph.add_edge('A', 'N')

    # Execute and display traversals starting from vertex 'B'
    start_vertex = 'B'
    bfs_result = graph.bfs(start_vertex)
    dfs_result = graph.dfs(start_vertex)

    print(f"Graph BFS (Start {start_vertex}):", " -> ".join(bfs_result))
    print(f"Graph DFS (Start {start_vertex}):", " -> ".join(dfs_result))