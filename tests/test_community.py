import sys
sys.path.append("src")

from graph import create_graph
from community import detect_communities


def test_detect_communities():
    G = create_graph()

    communities = detect_communities(G)

    assert len(communities) == 2
    assert sum(len(c) for c in communities) == 7