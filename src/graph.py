import networkx as nx


def create_graph():
    G = nx.Graph()

    edges = [
        ("A", "B"),
        ("A", "C"),
        ("B", "C"),
        ("B", "D"),
        ("C", "D"),
        ("E", "F"),
        ("E", "G"),
        ("F", "G"),
        ("D", "E")
    ]

    G.add_edges_from(edges)

    return G