from typing import Any

from queue import PriorityQueue
import networkx as nx

from src.plotting import plot_graph


def prim_mst(graph: nx.Graph, start_node="0") -> set[tuple[Any, Any]]:
    pqueue = PriorityQueue()
    edges_in_mst = set()
    nodes_on_mst = set()

    for neighbor in graph.neighbors(start_node):
        edge_weight = graph.get_edge_data(start_node, neighbor)["weight"]
        pqueue.put((edge_weight, (start_node, neighbor)))

    while len(nodes_on_mst) < len(G.nodes):
        _, edge = pqueue.get()

        if edge[0] not in nodes_on_mst:
            new_node = edge[0]
        elif edge[1] not in nodes_on_mst:
            new_node = edge[1]
        else:
            continue

        for neighbor in graph.neighbors(new_node):
            edge_weight = graph.get_edge_data(new_node, neighbor)["weight"]
            pqueue.put((edge_weight, (new_node, neighbor)))

        edges_in_mst.add(tuple(sorted(edge)))
        nodes_on_mst.add(new_node)

    return edges_in_mst


if __name__ == "__main__":
    G = nx.read_edgelist("./graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)

    edges = prim_mst(G, start_node="0")

    plot_graph(G, highlighted_edges=list(edges))
