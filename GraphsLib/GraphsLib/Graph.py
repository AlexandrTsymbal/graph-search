from functools import lru_cache


class Graph:
    """
    Graph class

    Creates an object of type "Graph"

    It is represented as a dictionary,
    where the key is the vertex index and the value is a list of pairs
    (adjacent vertex, path weight).

    You can define a graph manually by setting the "vertices" field by
    the number of vertices in your graph,
    then call ".add_edge(source, destination, weight)" sequentially.

    You can also specify a graph from a file or with input(),
    using ".from_file(path)" or "from_input()" as appropriate
    """

    def __init__(self):
        self.vertices = 0
        self.graph = {}

    def add_edge(self, source: int, destination: int, weight=1):
        """Adds an edge to an existing graph

            :param source: initial vertex
            :type source: int
            :param destination: final vertex
            :type destination: int
            :param weight: rib weight, defaults to 1
            :type weight: int
        """

        if source not in self.graph:
            self.graph[source] = []
        self.graph[source].append([destination, weight])

    def from_file(self, file_path):
        """defines a graph using the file

            :param file_path: path to file
            :type file_path: str
        """

        with open(file_path, 'r') as file:
            self.vertices = int(file.readline())
            source_ind = 1

            for line in file:
                vertexes = line.split()
                dest_ind = 1

                for vert in vertexes:
                    if int(vert) != 0:
                        self.add_edge(source_ind, dest_ind, int(vert))
                    dest_ind += 1

                source_ind += 1

    def extra_file(self, file_path: str, start: int = 1, finish: int = 2):
        with open(file_path, 'r') as file:
            self.vertices = int(file.readline())
            matrix = []

            for line in file:
                matrix.append(line.replace('\n', '').split(' '))

            visited_from_v = [False] * self.vertices
            visited_from_w = [False] * self.vertices

            def dfs_from_v(node):
                visited_from_v[node] = True
                for neighbor in range(self.vertices):
                    if matrix[node][neighbor] != '0':
                        if not visited_from_v[neighbor]:
                            dfs_from_v(neighbor)

            # Функция для поиска пути до w
            def dfs_to_w(node):
                visited_from_w[node] = True
                for neighbor in range(self.vertices):
                    if matrix[neighbor][node] != '0':
                        if not visited_from_w[neighbor]:
                            dfs_to_w(neighbor)

            # Начать обход из v
            dfs_from_v(start - 1)
            # Начать обход к w
            dfs_to_w(finish - 1)

            reachable_vertices = [i for i in range(self.vertices)
                                  if visited_from_v[i] and visited_from_w[i]]

            for i in range(self.vertices):
                if i not in reachable_vertices:
                    matrix[i] = ['0'] * self.vertices

                for j in range(self.vertices):
                    if matrix[i][j] != '0':
                        self.add_edge(i + 1, j + 1, int(matrix[i][j]))

            while True:
                vert_for_pop = None
                is_chain = False

                for vert in self.graph:
                    if len(self.graph[vert]) == 1:
                        next_vert = self.graph[vert][0][0]
                        plus_weight = self.graph[vert][0][1]
                        if next_vert in self.graph:
                            is_chain = True
                            self.graph[vert] = self.graph[next_vert]
                            for edge in self.graph[vert]:
                                edge[1] += plus_weight
                            vert_for_pop = next_vert
                            break

                if vert_for_pop is not None:
                    self.graph.pop(vert_for_pop)

                if not is_chain:
                    break

    def from_input(self):
        """sets the graph using the terminal"""

        self.vertices = int(input())
        for i in range(self.vertices):
            source_ind = i + 1
            dest_ind = 1
            for vert in input().split():
                if int(vert) != 0:
                    self.add_edge(source_ind, dest_ind, int(vert))
                dest_ind += 1

    def get_neighbors(self, vertex):
        """Returns the list of neighbors and the weight of the path
            to them from the given vertex

            :param vertex: vertex
            :type vertex: int

            :return: list of neighbors and the weight of the path to them
        """

        return self.graph.get(vertex, [])

    def get_vertices(self):
        """Returns a list of all vertices

        :return: list of all vertices
        """
        return list(self.graph.keys())

    def __str__(self):
        return str(self.graph)

    def right_argv(self, start: int, finish: int):
        """Checks vertices against the vertex list

        :param start: start vertex
        :type start: int
        :param finish: finish vertex
        :type finish: int
        :return: true or false depending on the test
        """

        return not ((start < 1 or start > self.vertices) or
                    (finish < 1 or finish > self.vertices))
