from typing import List


def create_graph(bridge_config: list, num_islands: int):

    graph = [[] for _ in range(num_islands + 1)]

    for [source, destination, distance] in bridge_config:
        graph[source].append((destination, distance))
        graph[destination].append((source, distance))

    return graph
