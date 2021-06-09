
# neighbors

from graph import create_graph


def test_create_a_graph_with_2_nodes():

    num_islands = 2
    bridge_config = [[1, 2, 1]]

    graph = create_graph(bridge_config, num_islands)

    assert graph == [[], [(2, 1)], [(1, 1)]]


def test_create_a_graph_with_3_nodes():

    num_islands = 3
    bridge_config = [[1, 2, 1], [3, 2, 3]]

    graph = create_graph(bridge_config, num_islands)

    assert graph == [[], [(2, 1)],
                     [(1, 1), (3, 3)],
                     [(2, 3)]]
