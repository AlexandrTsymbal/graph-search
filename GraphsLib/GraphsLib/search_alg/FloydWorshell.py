import sys

from GraphsLib.GraphsLib.Graph import Graph


def alg_fw(graph: Graph, start: int, finish: int) -> int | None:
    """Floyd-Worshell's algorithm for finding the shortest path from
        a vertex "start" to a vertex "finish" on a graph "graph"

    :param graph: the graph on which the shortest path is found
    :param start: initial vertex
    :param finish: finish vertex

    :return: minimum weight of this path
    """

    if not graph.right_argv(start, finish):
        print("Not right argv")
        return None

    distance = [sys.maxsize] * graph.vertices * graph.vertices
    for i in graph.graph:
        for neig in graph.graph[i]:
            distance[graph.vertices * (i - 1) + (neig[0] - 1)] = neig[1]

    for k in range(graph.vertices):
        for i in range(graph.vertices):
            for j in range(graph.vertices):
                vert = graph.vertices * i + j
                f_change = graph.vertices * i + k
                s_change = graph.vertices * k + j
                distance[vert] = min(distance[vert],
                                     distance[f_change] + distance[s_change])

    answ = distance[graph.vertices * (start - 1) + (finish - 1)]
    if answ == sys.maxsize:
        return 0
    else:
        return answ
