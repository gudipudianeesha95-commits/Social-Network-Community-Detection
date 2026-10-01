from graph import create_graph
from community import detect_communities, print_communities
from visualization import visualize_graph
from parallel import parallel_processing


def main():

    print("======================================")
    print(" SOCIAL NETWORK COMMUNITY DETECTION")
    print("======================================")

    G = create_graph()

    print("\nGraph Information")
    print("-----------------")
    print("Number of Users:", G.number_of_nodes())
    print("Number of Connections:", G.number_of_edges())

    communities = detect_communities(G)

    print_communities(communities)

    print("\nParallel Processing")
    print("-------------------")

    results = parallel_processing(list(G.nodes()))

    for result in results:
        print(result)

    visualize_graph(G, communities)

    print("\nGraph visualization saved in:")
    print("results/community_graph.png")

    print("\nProject completed successfully!")


if __name__ == "__main__":
    main()