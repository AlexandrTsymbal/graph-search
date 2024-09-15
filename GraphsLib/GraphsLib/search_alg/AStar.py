from GraphsLib.GraphsLib.Graph import Graph


def heuristic_cost_estimate(start, finish):
    """
    function to find heuristics based on vertex names

    :param start: initial vertex
    :param finish: finish vertex

    :return: heuristics
    """
    return abs(start - finish)


def alg_as(graph: Graph, start: int, finish: int) -> int | None:
    """A* algorithm for finding the shortest path from
        a vertex "start" to a vertex "finish" on a graph "graph"

    :param graph: the graph on which the shortest path is found
    :param start: initial vertex
    :param finish: finish vertex

    :return: minimum weight of this path
    """

    if not graph.right_argv(start, finish):
        print("Not right argv")
        return None

    # Список для отслеживания уже исследованных узлов
    # и которые нужно исследовать
    closed_set = set()
    open_set = [start]

    # Словари для отслеживания стоимости пути от начального узла
    # до данного узла и
    # предполагаемого пути относительно эвристики
    value_dict = {vertex: float('inf')
                  for vertex in range(1, graph.vertices+1)}
    value_dict[start] = 0

    expect_dict = {vertex: float('inf')
                   for vertex in range(1, graph.vertices+1)}
    expect_dict[start] = heuristic_cost_estimate(start, finish)

    while open_set:
        current = min(open_set, key=lambda x: expect_dict[x])

        if current == finish:
            return value_dict[finish]

        open_set.remove(current)
        closed_set.add(current)

        if current in graph.graph:
            for neighbor, weight in graph.graph[current]:
                if neighbor in closed_set:
                    continue

                tentative_value_dict = value_dict[current] + weight
                if tentative_value_dict < value_dict[neighbor]:
                    value_dict[neighbor] = tentative_value_dict
                    heur = heuristic_cost_estimate(neighbor, finish)
                    expect_dict[neighbor] = tentative_value_dict + heur
                    if neighbor not in open_set:
                        open_set.append(neighbor)

    return None
