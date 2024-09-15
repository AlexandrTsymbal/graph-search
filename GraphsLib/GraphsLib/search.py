from .search_alg import alg_di, alg_fw, alg_bf, alg_as, alg_js
from .Graph import Graph


def dij_alg(graph: Graph, start: int, finish: int):
    """Dijkstra's algorithm for finding the shortest path from
        a vertex "start" to a vertex "finish" on a graph "graph"

        :param graph: the graph on which the shortest path is found
        :param start: initial vertex
        :param finish: finish vertex

        :return: minimum weight of this path
    """
    return alg_di(graph, start, finish)


def bell_frd_alg(graph: Graph, start: int, finish: int):
    """Bellman-Ford's algorithm for finding the shortest path from
        a vertex "start" to a vertex "finish" on a graph "graph"

        :param graph: the graph on which the shortest path is found
        :param start: initial vertex
        :param finish: finish vertex

        :return: minimum weight of this path
    """
    return alg_bf(graph, start, finish)


def fld_wrsh_alg(graph: Graph, start: int, finish: int):
    """Floyd-Worshell's algorithm for finding the shortest path from
        a vertex "start" to a vertex "finish" on a graph "graph"

        :param graph: the graph on which the shortest path is found
        :param start: initial vertex
        :param finish: finish vertex

        :return: minimum weight of this path
    """
    return alg_fw(graph, start, finish)


def a_star_alg(graph: Graph, start: int, finish: int):
    """A* algorithm for finding the shortest path from
        a vertex "start" to a vertex "finish" on a graph "graph"

        :param graph: the graph on which the shortest path is found
        :param start: initial vertex
        :param finish: finish vertex

        :return: minimum weight of this path
    """
    return alg_as(graph, start, finish)


def jhn_alg(graph: Graph, start: int, finish: int):
    """Johnson's algorithm for finding the shortest path from
        a vertex "start" to a vertex "finish" on a graph "graph"

        :param graph: the graph on which the shortest path is found
        :param start: initial vertex
        :param finish: finish vertex

        :return: minimum weight of this path
    """
    return alg_js(graph, start, finish)
