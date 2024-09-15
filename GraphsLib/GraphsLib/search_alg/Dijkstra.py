import sys

from GraphsLib.GraphsLib.Graph import Graph


def alg_di(graph: Graph, start: int, finish: int) -> int | None:
    """Dijkstra's algorithm for finding the shortest path from
        a vertex "start" to a vertex "finish" on a graph "graph"

    :rtype: object
    :param graph: the graph on which the shortest path is found
    :param start: initial vertex
    :param finish: finish vertex

    :return: minimum weight of this path
    """

    if not graph.right_argv(start, finish):
        print("Not right argv")
        return None

    visited = [False] * graph.vertices
    distance = [sys.maxsize] * graph.vertices
    distance[start - 1] = 0

    while False in visited:
        for i in range(graph.vertices):
            if i + 1 in graph.graph:
                neighbors = graph.graph[i + 1]
                for neigh in neighbors:
                    ind = neigh[0]
                    distance[ind - 1] = min(distance[ind - 1],
                                            distance[i] + neigh[1])

            visited[i] = True
    return distance[finish - 1]
