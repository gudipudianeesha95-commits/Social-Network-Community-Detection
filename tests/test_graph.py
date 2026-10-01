import sys
sys.path.append("src")

from graph import create_graph


def test_create_graph():
    G = create_graph()

    assert G.number_of_nodes() == 7
    assert G.number_of_edges() == 9