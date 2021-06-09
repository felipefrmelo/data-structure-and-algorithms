import math
from queue import PriorityQueue


class Env:

    def __init__(self, map_n, goal=0) -> None:
        self.map = map_n
        self.goal = goal

    def get_node(self, node):
        return self.map.intersections[node]

    def actions(self, node):
        return map(lambda neighbor: (neighbor,
                                     self.calculate_path_cost(node, neighbor),
                                     self.calculate_heuristic(neighbor)
                                     ), self.map.roads[node])

    def calculate_heuristic(self, neighbor):
        return self.calculate_distance_between_nodes(
            self.goal, neighbor)

    def calculate_path_cost(self, node, neighbor):
        return self.calculate_distance_between_nodes(node, neighbor)

    def calculate_distance_between_nodes(self, node1, node2):
        return self.calculate_distance_between_two_points(
            self.get_node(node1), self.get_node(node2))

    def calculate_distance_between_two_points(self, p1, p2):
        delta_x = p2[0] - p1[0]
        delta_y = p2[1] - p1[1]
        return math.sqrt(delta_x**2 + delta_y**2)


class Path:

    def __init__(self, parent, value, path_cost=0, est_distance=0) -> None:
        self.parent = parent
        self.value = value
        self.path_cost = path_cost
        self.est_distance = est_distance
        self.f = path_cost + est_distance

    def __lt__(self, other):
        return self.f < other.f

    def path(self):

        result = []
        current = self
        while not current.parent is None:
            result = [current.value] + result
            current = current.parent

        return [current.value] + result


def shortest_path(M, start, goal):
    print("shortest path called")

    explored = [False for _ in M.intersections]
    queue = PriorityQueue()
    env = Env(M, goal)

    queue.put(Path(None, start))
    while not queue.empty():

        path = queue.get()

        if path.value == goal:
            return path.path()

        explored[path.value] = True

        for neighbor, distance, est_distance in env.actions(path.value):

            if not explored[neighbor]:
                queue.put(
                    Path(parent=path,
                         value=neighbor,
                         path_cost=distance + path.path_cost,
                         est_distance=est_distance))
