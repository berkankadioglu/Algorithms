from collections import defaultdict

class Graph:
    """
    For simplicity, assume connected graph ( each node is accessible by each other note )
    """
    def __init__(self):
        self.graph = defaultdict(set)

    def add_edge(self, u, v):
        self.graph[u].add(v)

    def depth_first_search(self, v, visited=set()):
        visited.add(v)
        print(v, end='_')
        for next_vertex in self.graph[v] - visited:
            self.depth_first_search(next_vertex, visited)

    def breadth_first_search(self, v, visited=set()):
        queue = [v]
        visited.add(v)

        while queue:
            s = queue.pop(0)
            print(s, end='_')

            for next_vertice in self.graph[s] - visited:
                queue.append(next_vertice)
                visited.add(next_vertice)


if __name__ == '__main__':

    g1 = Graph()
    g1.add_edge('a', 'b')
    g1.add_edge('a', 'c')
    g1.add_edge('b', 'a')
    g1.add_edge('b', 'd')
    g1.add_edge('c', 'a')
    g1.add_edge('c', 'd')
    g1.add_edge('d', 'e')
    g1.add_edge('e', 'a')

    g1.depth_first_search('a')
    print()
    g1.breadth_first_search('a')
