import queue
from typing import Any

import networkx as nx

from src.plotting import plot_graph


def visit(node: Any):
    print(f"Wow, it is {node} right here!")


def dfs_iterative(G: nx.Graph, node: Any):
    visited = {n: False for n in G}
    stack = queue.LifoQueue()
    stack.put(node)
    while not stack.empty():
        node = stack.get()
        if not visited[node]:
            visit(node)
            visited[node] = True
            for n_neigh in G.neighbors(node):
                stack.put(n_neigh)

def topoSortvisit(s, visited, list):

    visited[s] = True
    for i in G[s]:
        if not visited[i]:
            topoSortvisit(i, visited, list)
    list.insert(0, s)

def topological_sort(G: nx.DiGraph):
    visited = {n: False for n in G}
    list = []

    for v in G:
        if not visited[v]:
            topoSortvisit(v, visited, list)

    print(list)

if __name__ == "__main__":
    G = nx.read_edgelist("./graph_2.edgelist", create_using=nx.Graph)

    print("Iterative DFS")
    print("-" * 32)
    dfs_iterative(G, node="0")
    print()

    G = nx.read_edgelist(
        "./graph_2.edgelist", create_using=nx.DiGraph
    )
    plot_graph(G)
    print("Topological sort")
    print("-" * 32)
    topological_sort(G)
