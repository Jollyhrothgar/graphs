# Introduction

This is a pet project I'm working on to learn about graphs, implementing graph
algorithms, and building interactive graphs.

What needs to be built

- A library, representing graphs, nodes, edges
- A library, representing algorithms which can operate on graphs
- A library, for visualizing and interacting with graphs, including dynamically
  generating graphs

Other goals along the way

- Build and use logging to understand usage, failure modes, etc.

# Changelog

## 2019 Sep 10

Over the weekend, I played around with a few different ideas for representing
graphs and nodes, but I found myself getting into a chicken and egg kind of
loop. I would implement a node, and then start implementing edges for the node,
and then I would think, hey, I should make an edge class, but then when I would
implement an edge, then I would go back to implementing nodes. Conceptually, I
was trying to separate in code the concept of an edge and a node, but whole
point is that these things are connected. Maybe the best way to do it is to
create a graph class. But there are still problems here. What kind of graph? A
connected graph? A multigraph? A graph that has separate islands? These
decisions have to be made up front.

I would very much like to come up with my own implementation for graphs, but I
find myself totally lacking any intuition regarding how to do it. I guess I'm
probably dragging my feet for the usual reason - I want to make the perfect
implementation as a first step. This is impossible.

Anyway, then I got caught in another brain loop about how to represent graphs
internally - should I use a custom class, a linked list, a dictionary pointing
to lists, an adjacency list, or a adjacency matrix, and again, got caught in the
loop of trying to solve for the best representation before any code got written.

This lead me on a journey through many implementations and blogs about 'getting
started with graphs'. I know that there's already a graph library out there
(networkx) but my hope is to create something that is MINE (standing on the
shoulders of a billion other people...)

Some links I found useful:

-[Islands in a graph](https://www.geeksforgeeks.org/islands-in-a-graph-using-bfs/)
-[Graphs as a Python Class](https://www.python-course.eu/graphs_python.php)
-[Graph Representation](https://algorithms.tutorialhorizon.com/graph-representation-adjacency-matrix-and-adjacency-list/)
-[Graph and its Representations](https://www.geeksforgeeks.org/graph-and-its-representations/)
-[Graph Representations](https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/tutorial/)

Some direction now that I've done some research and failed to write and
functioning code:

- Support for multigraphs
- Support for multiple output representations
- Define a representation language that supports serialization
- Define a flexible attributes list that can be associated with nodes and edges
- Support unconnected graphs with islands
- Support for directed and undirected graphs
- Support for graph algorithms
- Physics based graph visualization (I wanna see bouncy nodes that wiggle in
  real time)
- Add setup.py in a bit (reference: [my distribution math library](https://github.com/Jollyhrothgar/distribution_math/tree/master/distribution_math))
