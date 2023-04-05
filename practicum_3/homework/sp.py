from typing import Any

import numpy as np
import networkx as nx

from src.plotting import plot_graph

def dijkstra_sp(G: nx.Graph, final_node: str, source_node="0") -> list[Any]:
    dist = {n: np.inf for n in G}
    shortest_paths = {}
    shortest_paths[source_node] = [source_node]
    dist[source_node] = 0
    visited = {n: False for n in G}

    for v in G:

        if not visited[v]:
            visited[v] = True

        for v_neigh in G.neighbors(v):
            if visited[v_neigh]:
                continue
            if dist[v_neigh] > dist[v] + G.edges[v, v_neigh]["weight"]:
                dist[v_neigh] = dist[v] + G.edges[v, v_neigh]["weight"]
                shortest_paths[v_neigh] = shortest_paths[v] + [v_neigh]

    return shortest_paths[final_node]


if __name__ == "__main__":
    G = nx.read_edgelist("./graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)
    final_node = "4"
    shortest_paths = dijkstra_sp(G, final_node, source_node="0")
    shortest_path_edges = [
        (shortest_paths[i], shortest_paths[i + 1])
        for i in range(len(shortest_paths) - 1)
    ]
    plot_graph(G, highlighted_edges=shortest_path_edges)
