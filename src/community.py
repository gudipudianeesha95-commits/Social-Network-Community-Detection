import networkx as nx


def detect_communities(G):
    communities = nx.community.greedy_modularity_communities(G)

    return [list(community) for community in communities]


def print_communities(communities):
    print("\nDetected Communities:")

    for i, community in enumerate(communities, start=1):
        print(f"Community {i}: {community}")