import pytest
from helpers import load_map
from student_code import shortest_path


@pytest.fixture
def map_10():
    return load_map('map-10.pickle')


@pytest.fixture
def map_40():
    return load_map('map-40.pickle')


def assertShortestPath(map_10, start, goal, expected):
    assert expected == shortest_path(map_10, start, goal)


def test_nearby_nodes(map_10):

    assertShortestPath(map_10, 8, 8, [8])
    assertShortestPath(map_10, 8, 9, [8, 9])
    assertShortestPath(map_10, 9, 8, [9, 8])


def test_with_a_node_in_the_middle_of_the_way(map_10, map_40):

    MAP_40_ANSWERS = [
        (12, 22, [12, 22]),
        (37, 28, [37, 12, 28]),
        (5, 34, [5, 16, 37, 12, 34]),
        (5, 5,  [5]),
        (8, 24, [8, 14, 16, 37, 12, 17, 10, 24])
    ]

    for start, goal, answer_path in MAP_40_ANSWERS:
        assertShortestPath(map_40, start, goal, answer_path)
