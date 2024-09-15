import sys

from GraphsLib.GraphsLib.Graph import Graph


def alg_js(graph: Graph, start: int, finish: int) -> int | None:
    """Johnson's algorithm for finding the shortest path from
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

    new_vert = graph.vertices + 1
    for i in range(1, new_vert):
        graph.add_edge(new_vert, i, 0)

    # Запускаем алгю Б-Ф для новой вершины
    distance = [sys.maxsize] * (graph.vertices + 1)
    distance[new_vert - 1] = 0

    list_edge = []
    for i in graph.graph:
        for neig in graph.graph[i]:
            list_edge.append((i - 1, neig[0] - 1, neig[1]))

    for i in range(graph.vertices - 1):
        for u, v, w in list_edge:
            if distance[u] != float("Inf") and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # Меняем вес ребер, чтобы не было отрицательных
    for verts in graph.graph.items():
        for weights in verts[1]:
            weights[1] = (weights[1] + distance[verts[0] - 1] -
                          distance[weights[0] - 1])

    # Запускаем Дейкстру ( O(|v|log(|v|)) ), так как у нас нет
    # больше отрицательных весов

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

    graph.graph.pop(graph.vertices + 1)
    return distance[finish - 1]
