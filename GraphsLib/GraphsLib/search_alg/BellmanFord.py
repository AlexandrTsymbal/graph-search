import sys
from GraphsLib.GraphsLib.Graph import Graph


def alg_bf(graph: Graph, start: int, finish: int) -> int | None:
    """Bellman-Ford's algorithm for finding the shortest path from
        a vertex "start" to a vertex "finish" on a graph "graph"

    :param graph: the graph on which the shortest path is found
    :param start: initial vertex
    :param finish: finish vertex

    :return: minimum weight of this path
    """

    if not graph.right_argv(start, finish):
        print("Not right argv")
        return None

    distance = [sys.maxsize] * graph.vertices
    distance[start - 1] = 0

    list_edge = []
    for i in graph.graph:
        for neig in graph.graph[i]:
            list_edge.append((i - 1, neig[0] - 1, neig[1]))

    for i in range(graph.vertices - 1):
        for u, v, w in list_edge:
            if distance[u] != float("Inf") and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    for u, v, w in list_edge:
        if distance[u] != float("Inf") and distance[u] + w < distance[v]:
            print("Graph contains negative weight cycle")
            return None

    return distance[finish - 1]
