from graph import create_graph
from queue import PriorityQueue


def get_minimum_cost_of_connecting(num_islands, bridge_config):
    """
    :param: num_islands - number of islands
    :param: bridge_config - bridge configuration as explained in the problem statement
    return: cost (int) minimum cost of connecting all islands
    TODO complete this method to returh minimum cost of connecting all islands
    """

    priorityQueue = PriorityQueue()

    graph = create_graph(bridge_config, num_islands)

    priorityQueue.put((1, 0))

    visited = [False for _ in range(num_islands + 1)]
    total_cost = 0

    while not priorityQueue.empty():

        island, edge_cost = priorityQueue.get()

        if(visited[island]):
            continue

        total_cost += edge_cost

        for neighbour in graph[island]:
            priorityQueue.put(neighbour)

        visited[island] = True

    return total_cost
