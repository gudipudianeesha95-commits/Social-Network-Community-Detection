import networkx as nx
import matplotlib.pyplot as plt


def visualize_graph(G, communities):

    plt.figure(figsize=(8, 6))

    pos = nx.spring_layout(G, seed=42)

    colors = {}

    for i, community in enumerate(communities):
        for node in community:
            colors[node] = i

    node_colors = [colors[node] for node in G.nodes()]

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        node_size=1000,
        font_size=12
    )

    plt.title("Social Network Community Detection")

    plt.savefig("results/community_graph.png")

    plt.show()