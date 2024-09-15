# Graphs Library #

## What is this? ##

A simple library for finding the shortest path in a graph by different algorithms.

----------

## Using ##

Using the library is as simple and convenient as possible:

Let's import it first:
First, import everything from the library (use the `from `...` import *` construct).

### Examples of all operations: ###

_Creating an empty graph:_

    graph = Graph()

Filling the graph using a file:

    graph.from_file('matrix.txt')

Filling in the graph using the terminal:

    graph.from_input()

Finding the lowest route weight using Dijkstra's algorithm:

    dij_alg(graph, 1, 2)

Finding the lowest route weight using "Bellman-Ford's algorithm:

    bell_frd_alg(g1, 1, 3)

Finding the lowest route weight using Floyd-Worshell's algorithm:

    fld_wrsh_alg(g1, 1, 4)

Finding the lowest route weight using Floyd-Worshell's algorithm:

    a_star_alg(g1, 1, 4)

## Work algorithms: ##

### Dijkstra's algorithm ###
Dijkstra's algorithm finds the shortest paths from one source vertex to all other vertices in a graph with non-negative edge weights.

Main steps:

1. Initialization: we set the distance 0 to the initial vertex and infinity to all other vertices.
2. Choose the vertex with the smallest known distance and mark it as visited.
3. We update the distances to its neighbors: if the path through the current vertex is shorter, we update it.
4. Repeat steps 2-3 until all vertices are visited or all target vertices are reached.

The algorithm terminates when all vertices are visited or there are no available vertices with finite distance.

### Bellman-Ford's algorithm ###
The Bellman-Ford algorithm finds the shortest paths from one source vertex to all others in a graph, including graphs with negative edge weights.

The main steps are:
1. Initialization: we set the initial vertex to distance 0 and all others to infinity.
2. Repeat \(V-1\) times (where \(V\) is the number of vertices): for each edge we update the distance to its end if the path through its beginning is shorter.
3. Checking for negative weight cycles: go through all edges to find possible distance decreases.

The algorithm terminates if no reductions are found at the last step.

### Floyd-Worshell's algorithm ###
The Floyd-Worshell algorithm finds the shortest paths between all pairs of vertices in a graph.

The main steps are:
1. Initialization: create a distance matrix where the element \((i, j)\) is the weight of the edge between vertices \(i\) and \(j\) (infinity if there is no edge). The diagonal elements are zero.
2. For each vertex \(k\) we update the distance matrix: for each pair of vertices \((i, j)\) we check whether the path through \(k\) is shorter than the current known path.
3. Repeat step 2 for all vertices of \(k\).

The algorithm terminates when all vertices have been processed. The result is the matrix of shortest paths between all pairs of vertices.

### A* algorithm ###
The A* (A-star) algorithm is used to find the shortest path in a graph, especially in path finding problems in maps.

The basic steps are:
1. Initialization: we create an open list in which we place an initial vertex. The initial vertex has a cost f = g + h, where g is the distance from the initial vertex and h is a heuristic estimate of the distance to the target vertex.
2. As long as the open list is not empty:
   - We extract the vertex with the lowest cost f.
   - If this is the target vertex, the path is found.
   - We move this vertex to the closed list and examine its neighbors.
   - For each neighbor we compute g and f. If the new path to the neighbor is shorter than the known one, we update the path and add the neighbor to the open list (if it is not there yet).
3. The algorithm terminates when the target vertex is found or the open list is empty (no path).

A* guarantees to find the shortest path if the heuristic is valid (never overestimates the distance).

### Johnson's algorithm ###
Johnson's algorithm is used to find the shortest paths between all pairs of vertices in a graph that can contain edges with negative weights (but no negative weight cycles).

The basic steps are:
1. Add a new vertex s and connect it by edges with weight 0 to all vertices in the graph.
2. We use the Bellman-Ford algorithm, starting from vertex s, to compute the shortest distance h(v) from s to each vertex v. The Bellman-Ford algorithm is used to compute the shortest distance h(v) from s to each vertex v. If a negative weight cycle is detected, the algorithm stops.
3. Recalculate the weights of the edges of the graph: for each edge (u, v), a new weight w'(u, v) = w(u, v) + h(u) - h(v). These new weights are non-negative.
4. We remove the vertex s and its edges.
5. For each vertex v, use Dijkstra's algorithm to find the shortest paths to all other vertices in the graph with the recalculated edge weights.
6. Reconstruct the original weights: for each path d'(u, v) found, recalculate it back to the original weights using the formula d(u, v) = d'(u, v) - h(u) + h(v).

The algorithm terminates by providing the matrix of shortest paths between all pairs of vertices.

----------

## Developer ##

Telegram: [_**Sanchezzzz300**_](https://t.me/sanchezzzz300) 